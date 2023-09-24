import sys, os, datetime, tqdm, shutil
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QAbstractTableModel, Qt, QSortFilterProxyModel
import pandas as pd
import DOCX_feature_extraction as dfe
import DOCX_DataPreprocessing as DP
from WORD_main import Ui_WORD
import numpy as np

np.random.seed(42)
from numpy import linalg
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
import functools
from PyQt5.QtCore import QThread, pyqtSignal


## 전처리 프로세스 클래스
class PreProcessingThread(QThread):
    progress_updated = pyqtSignal(int)

    def __init__(self, folder_path, output_path):
        super().__init__()
        self.folder_path = folder_path
        self.output_path = output_path

    def run(self):
        dataframe = pd.DataFrame()
        countfile = 0
        file_count = sum([len(files) for _, _, files in os.walk(self.folder_path)])
        print(file_count)

        for dirname, _, file_names in os.walk(self.folder_path):
            for i, file_name in enumerate(file_names):
                file_path = os.path.join(dirname, file_name)
                try:
                    extracted_data = dfe.feature_extraction(file_path)
                    extracted_data = pd.DataFrame([extracted_data])
                    dataframe = pd.concat([dataframe, extracted_data], ignore_index=True)
                except Exception as e:
                    print(file_name, str(e))
                countfile += 1
                progress = int((countfile * 100) / file_count)
                self.progress_updated.emit(progress)

        now = datetime.datetime.now()
        outputcsv = os.path.join(
            self.output_path,
            f"[{now.strftime('%Y%m%d')}] preprocessing_{os.path.basename(self.folder_path)}.csv"
        )
        DP.datapreprocessing(dataframe, outputcsv)


# dataframe 을 columnview 에 띄우는 데 필요한 Class 선언
class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow):
    # 워드 파일이 모여 있는 폴더 경로 선택
    def FolderPath_Click(self):
        FolderPath = QFileDialog.getExistingDirectory(self, 'Select Directory"')
        if FolderPath != '':
            self.ui.folder_path.setText(FolderPath)
        else:
            QMessageBox.about(self, "Error", "Not selected!")
        print("워드 파일이 모여 있는 폴더 경로 선택 ")

    # 전처리된 파일 출력 하는 경로
    def OutputPath_Click(self):
        outputpath = QFileDialog.getExistingDirectory(self, 'Select Directory"')
        if outputpath != '':
            self.ui.output_Path.setText(outputpath)
        else:
            QMessageBox.about(self, "Error", "Not selected!")
        print("전처리된 파일 출력 하는 경로 ")

    # 전처리된 파일 선택하기
    def preprocessing_fileselect_Click(self):
        FolderPath = self.ui.output_Path.displayText()
        file_name, _ = QFileDialog.getOpenFileName(self, 'PreProcessing File Load', FolderPath,
                                                   'All File(*);; 전처리된 파일(*.csv)')
        if file_name != '':
            file_title = os.path.basename(file_name)
            self.ui.preprocessing_filename.setText(file_title)

            # csv에서 데이터 불러오기
            self.ui.preProcessFile = file_name
            select_data = pd.read_csv(file_name, encoding='utf-8', engine='python')
            self.ui.TableViewData = PandasModel(select_data[['file_name']])
            self.ui.fulldataView.setModel(self.ui.TableViewData)

            self.ui.feature_count.setRange(0, len(select_data.columns))
            self.ui.feature_count.setSingleStep(1)
            self.ui.feature_count.setValue(len(select_data.columns))
        else:
            QMessageBox.about(self, "Error", "Not selected!")

    def fulldataViewmouseClickEvent(self):
        row = self.ui.fulldataView.currentIndex().row()
        column = self.ui.fulldataView.currentIndex().column()
        model = self.ui.fulldataView.model()
        data = model.data(model.index(row, column))
        self.ui.selectopenfile_name = data
        self.ui.selectFileName.setText(data)

    def dataViewmouseClickEvent(self):
        row = self.ui.dataView.currentIndex().row()
        column = self.ui.dataView.currentIndex().column()
        model = self.ui.dataView.model()
        data = model.data(model.index(row, column))
        self.ui.selectopenfile_name = data

    def search_similarity_Click(self):
        self.ui.selectFileName.setText(self.ui.selectopenfile_name)
        file_title = self.ui.selectFileName.displayText()
        # input_csvfile = self.ui.preprocessing_filename.displayText()
        print("검색 대상 파일 : ", file_title)
        if file_title != '':
            accuracy_ratio = float(self.ui.similarity_ratio.text()) / 100

            # csv에서 데이터 불러오기
            select_data = pd.read_csv(self.ui.preProcessFile, encoding='utf-8', engine='python')
            select_data.set_index('file_name', inplace=True, drop=True)

            # 전체 피처
            matrix = select_data

            # Data 스케일링 방법 체크
            if self.ui.Feature.isChecked():
                ## 피처 중요도 도입
                feature_count = int(self.ui.feature_count.text()) if int(self.ui.feature_count.text()) < len(
                    matrix.columns) else len(matrix.columns)
                # importance_rate = [10.52631579,9.941520468,9.356725146,8.771929825,8.187134503,7.602339181,7.01754386,6.432748538,5.847953216,5.263157895,4.678362573,4.093567251,3.50877193,2.923976608,2.339181287,1.754385965,1.169590643,0.584795322]
                select = matrix.columns
                # ["paragraph_name", "character_name", "table_name", "numbering_name", "fontList", "sectPr_pgMar_top", "sectPr_pgMar_right", "sectPr_pgMar_bottom", "sectPr_pgSz_w", "sectPr_pgSz_h", "sectPr_pgMar_left", "sectPr_pgMar_header", "sectPr_pgMar_footer", "pPrDefault_spacing_after", "pPrDefault_spacing_line", "abstractNum"]
                matrix = matrix[select[:feature_count]]  # * importance_rate[:feature_count]
            else:
                print("Feature Not checked")

            std_scaler = StandardScaler()
            std_data = matrix.copy()
            std_scaler.fit(std_data)
            data_x = pd.DataFrame(std_scaler.transform(std_data))
            matrix = data_x.set_index(std_data.index)

            normalizer = Normalizer()
            normal_data = matrix.copy()
            normal_data[:] = normalizer.fit_transform(normal_data[:])
            matrix = normal_data

            # 유사도 측정 알고리즘 방법 체크
            algorithm = self.ui.algo_select.currentText()
            if algorithm == "Cosine":
                article = matrix.loc[file_title]
                similarities = matrix.dot(article)
                Cosine_debug = pd.DataFrame(similarities.copy())
                Cosine_debug = Cosine_debug.sort_values(by=[0], ascending=False)
                matrix = Cosine_debug[Cosine_debug[0] > accuracy_ratio]
            elif algorithm == "Euclidean":
                tmp_euclidean = matrix.copy()
                tmp_euclidean = pd.DataFrame(linalg.norm(tmp_euclidean.values, ord=1, axis=1), columns=['Simularity'],
                                             index=matrix.index)
                tmp_euclidean['Simularity'] = abs(
                    tmp_euclidean['Simularity'] - tmp_euclidean['Simularity'][file_title]) * 100
                matrix = tmp_euclidean.sort_values(by=['Simularity'], ascending=True)
            elif algorithm == "Menhatem":
                tmp_menhatem = matrix.copy()
                tmp_menhatem = pd.DataFrame(linalg.norm(tmp_menhatem.values, ord=1, axis=1), columns=['Simularity'],
                                            index=matrix.index)
                tmp_menhatem['Simularity'] = abs(
                    tmp_menhatem['Simularity'] - tmp_menhatem['Simularity'][file_title]) * 100
                matrix = tmp_menhatem.sort_values(by=['Simularity'], ascending=True)
            elif algorithm == "Pearson_Correlation":
                article = matrix.loc[file_title]
                similarities = matrix.corrwith(article, axis=1, method='pearson')
                Pearson_debug = pd.DataFrame(similarities.copy())
                Pearson_debug = Pearson_debug.sort_values(by=[0], ascending=False)
                matrix = Pearson_debug[Pearson_debug[0] > accuracy_ratio]
            else:
                print("ALGORITHM SELECT ERROR")

            # 컬럼 뷰에 보이기 dataframe 보이기
            matrix.columns = ["Similarity"]
            self.ui.dataView.setModel(PandasModel(matrix.reset_index()))
        else:
            QMessageBox.about(self, "Error", "Not selected!")

    # 추출할 CSV 파일
    def ExportCSV_Click(self):
        output_path = self.ui.output_Path.displayText()
        file_name = os.path.basename(self.ui.selectFileName.displayText())
        export_output_path = os.path.join(output_path, f"{self.ui.algo_select.currentText()}_{file_name}.csv")

        try:
            data = pd.DataFrame(self.ui.dataView.model()._data)
            pre_processed_data = pd.read_csv(self.ui.preProcessFile, encoding='utf-8', engine='python')
            exported_data = data.join(pre_processed_data.set_index('file_name'), on='file_name')
            exported_data = exported_data.set_index('file_name')

            exported_data.to_csv(export_output_path, encoding='utf-8-sig')

            QMessageBox.about(self, "Export CSV", f"Output Path is \n{export_output_path}")
        except:
            QMessageBox.about(self, "Export CSV ERROR", f"NOT EXPORT DATA")

    def filter(self, filter_text, ):

        proxy_model = QSortFilterProxyModel()
        proxy_model.setSourceModel(self.ui.TableViewData)
        self.ui.fulldataView.setModel(proxy_model)
        proxy_model.setFilterFixedString(filter_text)
        proxy_model.setFilterKeyColumn(0)

    def FileOpen_Click(self):
        # fileopenpath = self.ui.folder_path.displayText() + "/" + self.ui.selectopenfile_name
        fileopenpath = self.ui.selectopenfile_name

        try:
            os.startfile(fileopenpath)
        except:
            QMessageBox.about(self, "FileOpen ERROR", fileopenpath)

    def start_preprocessing(self):
        self.thread = PreProcessingThread(self.ui.folder_path.displayText(), self.ui.output_Path.displayText())
        self.thread.progress_updated.connect(self.ui.progress_bar.setValue)
        self.thread.finished.connect(self.processing_finished)
        self.thread.start()
        self.ui.PreProcessing.setEnabled(False)

    def processing_finished(self):
        self.ui.PreProcessing.setEnabled(True)
        self.thread = None
        QMessageBox.information(self, "Pre-processing Finished", "Pre-processing finished successfully!")

    def __init__(self):
        super().__init__()
        self.ui = Ui_WORD()
        self.ui.setupUi(self)
        self.ui.TableViewData = None
        self.ui.selectopenfile_name = None
        self.ui.preProcessFile = None

        self.ui.progress_bar.setValue(0)
        self.ui.similarity_ratio.setRange(-100.0, 100.0)
        self.ui.similarity_ratio.setSingleStep(1.0)
        self.ui.similarity_ratio.setValue(97.0)

        self.ui.feature_count.setRange(0, 0)
        self.ui.feature_count.setSingleStep(1)
        self.ui.feature_count.setValue(0)
        self.thread = None

        self.ui.dataView.setSortingEnabled(True)
        self.ui.dataView.sortByColumn(0, Qt.AscendingOrder)
        self.ui.fulldataView.setSortingEnabled(True)
        self.ui.fulldataView.sortByColumn(0, Qt.AscendingOrder)

        self.ui.FolderPath.clicked.connect(self.FolderPath_Click)
        self.ui.OutputPath.clicked.connect(self.OutputPath_Click)
        self.ui.PreProcessing.clicked.connect(self.start_preprocessing)
        self.ui.preprocess_file.clicked.connect(self.preprocessing_fileselect_Click)
        self.ui.fulldataView.clicked.connect(self.fulldataViewmouseClickEvent)
        self.ui.dataView.clicked.connect(self.dataViewmouseClickEvent)
        self.ui.search_similarity.clicked.connect(self.search_similarity_Click)
        self.ui.export_csv.clicked.connect(self.ExportCSV_Click)
        self.ui.fileopen.clicked.connect(self.FileOpen_Click)

        # 검색 창 활성화
        filter_with_model = functools.partial(self.filter)
        self.ui.SearchFileName.textChanged.connect(filter_with_model)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()