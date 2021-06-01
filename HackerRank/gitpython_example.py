import git
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class gitRepo:
    def __init__(self, repoPath):
        self._repo = git.Repo(repoPath)

    def listFiles(self):
        res = []

        return _utilListFiles(self)



if __name__ == '__main__':
    logger.info('enter main cwd ={}'.format(os.getcwd()))
    repo = git.Repo('C:\\Users\\prade\\work\\GitHub\\practice_python')
    for i in next(repo.iter_trees()).list_traverse():
        logger.info('enter main cwd ={}'.format(os.getcwd()))
        logger.info(os.path.relpath(i.abspath))
        logger.info('==============')