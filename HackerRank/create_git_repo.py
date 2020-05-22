import git
import os
import shutil


if __name__ == '__main__':
    # change to work dir
    os.chdir('..\..\..')

    """
    # create repo
    repo_dir = os.path.join(os.getcwd() + '\\tmp_git_repo')
    shutil.rmtree(repo_dir, True)
    repo = git.Repo.init(repo_dir, bare=True)

    clone_dir = os.path.join(os.getcwd() + '\\tmp_git_repo_clone')
    shutil.rmtree(clone_dir, True)
    cloned_repo = git.Repo.clone_from(repo_dir, clone_dir)

    file_name = os.path.join(clone_dir, 'file.txt')
    file_handle = open(file_name, "a")
    file_handle.write('line {} in {}\n'.format(0, file_name))
    file_handle.close()
    cloned_repo.index.add([file_name])
    cloned_repo.index.commit("{}-th commit for {}".format(0, file_name))
    cloned_repo.remote("origin").push()

    # create clone
    cloned_repo_l = list()
    for k in range(1000):
        clone_dir = os.path.join(os.getcwd(), 'tmp_git_repo_clone{}'.format(k))
        os.system('rmdir /S /Q {}'.format(clone_dir))
        cloned_repo = git.Repo.clone_from(repo_dir, clone_dir)
        cloned_repo_l.append(cloned_repo)

        # commit files
        for i in range(100):
            file_name = os.path.join(clone_dir, 'file'+str(k*100+i)+'.txt')
            for j in range(2):
                file_handle = open(file_name, "a")
                file_handle.write('line {} in {}\n'.format(j, file_name))
                file_handle.close()
                cloned_repo.index.add([file_name])
                cloned_repo.index.commit("{}-th commit for {}".format(j, file_name))

    for k in range(1000):
        if k:
            os.system('rmdir /S /Q "tmp_git_repo_clone{}"'.format(k - 1))
        cloned_repo_l[k].git.pull('--rebase')
        cloned_repo_l[k].remote("origin").push()
    """

    for k in range(97, 1000):
        if k:
            os.system('rmdir /S /Q "tmp_git_repo_clone{}"'.format(k - 1))
        os.chdir('tmp_git_repo_clone{}'.format(k))
        os.system('git pull --rebase')
        os.system('git push')
        os.chdir('..')