# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WORD_mainPglKID.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class Ui_WORD(object):
    def setupUi(self, WORD):
        if not WORD.objectName():
            WORD.setObjectName(u"WORD")
        WORD.resize(1203, 894)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WORD.sizePolicy().hasHeightForWidth())
        WORD.setSizePolicy(sizePolicy)
        self.actionEXIT_Q = QAction(WORD)
        self.actionEXIT_Q.setObjectName(u"actionEXIT_Q")
        self.centralwidget = QWidget(WORD)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.OutputPath = QPushButton(self.centralwidget)
        self.OutputPath.setObjectName(u"OutputPath")

        self.gridLayout.addWidget(self.OutputPath, 2, 2, 1, 1)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.gridLayout.addWidget(self.progress_bar, 3, 0, 1, 2)

        self.FolderPath = QPushButton(self.centralwidget)
        self.FolderPath.setObjectName(u"FolderPath")
        self.FolderPath.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.FolderPath, 1, 2, 1, 1)

        self.PreProcessing = QPushButton(self.centralwidget)
        self.PreProcessing.setObjectName(u"PreProcessing")

        self.gridLayout.addWidget(self.PreProcessing, 3, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMargin(10)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3)

        self.output_Path = QLineEdit(self.centralwidget)
        self.output_Path.setObjectName(u"output_Path")

        self.gridLayout.addWidget(self.output_Path, 2, 0, 1, 1)

        self.folder_path = QLineEdit(self.centralwidget)
        self.folder_path.setObjectName(u"folder_path")

        self.gridLayout.addWidget(self.folder_path, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.similarity_ratio = QDoubleSpinBox(self.centralwidget)
        self.similarity_ratio.setObjectName(u"similarity_ratio")
        self.similarity_ratio.setAccelerated(True)

        self.gridLayout_3.addWidget(self.similarity_ratio, 10, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 9, 1, 1, 1)

        self.feature_count = QSpinBox(self.centralwidget)
        self.feature_count.setObjectName(u"feature_count")
        self.feature_count.setMaximum(55)

        self.gridLayout_3.addWidget(self.feature_count, 10, 2, 1, 1)

        self.algo_select = QComboBox(self.centralwidget)
        self.algo_select.addItem("")
        self.algo_select.addItem("")
        self.algo_select.setObjectName(u"algo_select")

        self.gridLayout_3.addWidget(self.algo_select, 10, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 9, 2, 1, 1)

        self.Feature = QCheckBox(self.centralwidget)
        self.Feature.setObjectName(u"Feature")
        self.Feature.setEnabled(True)
        self.Feature.setChecked(True)

        self.gridLayout_3.addWidget(self.Feature, 8, 2, 1, 1)

        self.simularity_title = QLabel(self.centralwidget)
        self.simularity_title.setObjectName(u"simularity_title")

        self.gridLayout_3.addWidget(self.simularity_title, 9, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 2)

        self.title2 = QLabel(self.centralwidget)
        self.title2.setObjectName(u"title2")
        self.title2.setMargin(10)

        self.gridLayout_2.addWidget(self.title2, 1, 0, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.export_csv = QPushButton(self.centralwidget)
        self.export_csv.setObjectName(u"export_csv")

        self.gridLayout_6.addWidget(self.export_csv, 6, 13, 1, 1)

        self.SearchFileName = QLineEdit(self.centralwidget)
        self.SearchFileName.setObjectName(u"SearchFileName")

        self.gridLayout_6.addWidget(self.SearchFileName, 1, 1, 1, 6)

        self.fulldataView = QTableView(self.centralwidget)
        self.fulldataView.setObjectName(u"fulldataView")
        self.fulldataView.setAutoFillBackground(False)
        self.fulldataView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.fulldataView.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.fulldataView.setSortingEnabled(True)
        self.fulldataView.horizontalHeader().setCascadingSectionResizes(False)
        self.fulldataView.horizontalHeader().setStretchLastSection(True)
        self.fulldataView.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_6.addWidget(self.fulldataView, 3, 0, 1, 7)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)

        self.preprocess_file = QPushButton(self.centralwidget)
        self.preprocess_file.setObjectName(u"preprocess_file")
        self.preprocess_file.setMaximumSize(QSize(254, 16777215))
        self.preprocess_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.preprocess_file.setAutoRepeatDelay(300)

        self.gridLayout_6.addWidget(self.preprocess_file, 0, 6, 1, 1)

        self.search_similarity = QPushButton(self.centralwidget)
        self.search_similarity.setObjectName(u"search_similarity")

        self.gridLayout_6.addWidget(self.search_similarity, 6, 6, 1, 1)

        self.preprocessing_filename = QLineEdit(self.centralwidget)
        self.preprocessing_filename.setObjectName(u"preprocessing_filename")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.preprocessing_filename.sizePolicy().hasHeightForWidth())
        self.preprocessing_filename.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.preprocessing_filename, 0, 0, 1, 6)

        self.fileopen = QPushButton(self.centralwidget)
        self.fileopen.setObjectName(u"fileopen")

        self.gridLayout_6.addWidget(self.fileopen, 6, 5, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_5, 1, 7, 1, 1)

        self.selectFileName = QLineEdit(self.centralwidget)
        self.selectFileName.setObjectName(u"selectFileName")

        self.gridLayout_6.addWidget(self.selectFileName, 1, 8, 1, 6)

        self.dataView = QTableView(self.centralwidget)
        self.dataView.setObjectName(u"dataView")
        self.dataView.setMinimumSize(QSize(5, 0))
        self.dataView.setMaximumSize(QSize(16777215, 16777215))
        self.dataView.setSortingEnabled(True)
        self.dataView.horizontalHeader().setCascadingSectionResizes(False)
        self.dataView.horizontalHeader().setStretchLastSection(True)
        self.dataView.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_6.addWidget(self.dataView, 3, 7, 1, 7)


        self.gridLayout_4.addLayout(self.gridLayout_6, 2, 0, 1, 1)

        WORD.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WORD)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1203, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        WORD.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(WORD)
        self.statusbar.setObjectName(u"statusbar")
        WORD.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionEXIT_Q)

        self.retranslateUi(WORD)

        QMetaObject.connectSlotsByName(WORD)
    # setupUi

    def retranslateUi(self, WORD):
        WORD.setWindowTitle(QCoreApplication.translate("WORD", u"Word Search", None))
        self.actionEXIT_Q.setText(QCoreApplication.translate("WORD", u"EXIT(Q)", None))
        self.OutputPath.setText(QCoreApplication.translate("WORD", u"\ucd9c\ub825\ud30c\uc77c\uacbd\ub85c", None))
        self.FolderPath.setText(QCoreApplication.translate("WORD", u"\ud3f4\ub354 \uacbd\ub85c", None))
        self.PreProcessing.setText(QCoreApplication.translate("WORD", u"\uc804\ucc98\ub9ac \uc2dc\uc791", None))
        self.label_3.setText(QCoreApplication.translate("WORD", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">\uc6cc\ub4dc \ud30c\uc77c \uc804\ucc98\ub9ac</span></p></body></html>", None))
        self.similarity_ratio.setSpecialValueText(QCoreApplication.translate("WORD", u"97", None))
        self.label.setText(QCoreApplication.translate("WORD", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\uc720\uc0ac \uce21\uc815 \uae30\uc900 </span></p></body></html>", None))
        self.algo_select.setItemText(0, QCoreApplication.translate("WORD", u"Cosine", None))
        self.algo_select.setItemText(1, QCoreApplication.translate("WORD", u"Pearson_Correlation", None))

        self.label_2.setText(QCoreApplication.translate("WORD", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\uc0ac\uc6a9\ud558\ub294 \ud53c\ucc98 \uac1c\uc218</span></p></body></html>", None))
        self.Feature.setText(QCoreApplication.translate("WORD", u"Feature \uc120\uc815", None))
        self.simularity_title.setText(QCoreApplication.translate("WORD", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\uc720\uc0ac\ub3c4 \uce21\uc815 \uc54c\uace0\ub9ac\uc998</span></p></body></html>", None))
        self.title2.setText(QCoreApplication.translate("WORD", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">\uc6cc\ub4dc \ud30c\uc77c \uc720\uc0ac\ub3c4 \uac80\uc0c9</span></p></body></html>", None))
        self.export_csv.setText(QCoreApplication.translate("WORD", u"Export CSV", None))
        self.label_4.setText(QCoreApplication.translate("WORD", u"<html><head/><body><p align=\"center\">\uac80\uc0c9 : </p></body></html>", None))
        self.preprocess_file.setText(QCoreApplication.translate("WORD", u"\ud30c\uc77c \ub85c\ub4dc", None))
        self.search_similarity.setText(QCoreApplication.translate("WORD", u"\uac80\uc0c9", None))
        self.fileopen.setText(QCoreApplication.translate("WORD", u"\ud30c\uc77c \uc5f4\uae30", None))
        self.label_5.setText(QCoreApplication.translate("WORD", u"\uac80\uc0c9 \ub300\uc0c1 \ud30c\uc77c \uba85: ", None))
        self.menuFile.setTitle(QCoreApplication.translate("WORD", u"File", None))
    # retranslateUi

