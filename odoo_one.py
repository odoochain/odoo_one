#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import main_window
import logging
import getopt
import sys
from PyQt5 import QtWidgets

root_logger = logging.getLogger()
root_logger.setLevel("INFO")
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root_logger.addHandler(handler)
logger = logging.getLogger(__name__)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hdp:s:", ["help", "debug", "db-path=", "style="])
    except getopt.GetoptError as e:
        logger.error(e)
        print_help()
        sys.exit(2)

    db_path = ''
    style_name = ''
    for opt, arg in opts:
        if opt in ("-d", "--debug"):
            root_logger.setLevel("DEBUG")
            logger.debug("Debug mode ON")
        elif opt in ("-p", "--db-path"):
            db_path = arg
        elif opt in ("-s", "--style"):
            style_name = arg
        elif opt in ("-h", "--help"):
            print_help()
            sys.exit()

    sys.argv = [sys.argv[0]]
    logger.info("Odoo One starting...")
    app = QtWidgets.QApplication(sys.argv)

    app.setApplicationName("Odoo One")

    # logger.info("Loading translations...")
    # tr = translators(app)
    # localeLanguage = QtCore.QLocale.system().name()
    # tr.installTranslators(localeLanguage)


    logger.info('Showing main window...')
    ui_main = main_window.MainWindow()
    ui_main.setupUi()
    ui_main.show()

    logger.info("Go!")
    app.exec()



    sys.exit()


def print_help():
    help_str = '''
    
#########################    
#    Odoo One Help      #
#########################

    Parameters:
        -d, --debug:       Enable debug mode
        -s, --style:       Set Qt Style (Windows, Fusion...)
        -p, --db-path:     Set the database file path (~/.local/share/pyzik/data/pyzik.db)
        -h, --help:        Display help
        
    '''
    logger.info(help_str)


if __name__ == "__main__":
    main()