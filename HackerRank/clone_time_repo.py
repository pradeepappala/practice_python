import git
import os
import shutil
import timeit


if __name__ == '__main__':
    # change to work dir
    os.chdir('..\..')

    clone_dir = os.path.join(os.getcwd() + '\\tmp_git_repo_clone')

    os.system('rmdir /S /Q {}'.format(clone_dir))
    start_time = timeit.default_timer()
    cloned_repo = git.Repo.clone_from(os.path.join(os.getcwd() + '\\practice_python'), clone_dir)
    print('completed in {}'.format(timeit.default_timer() - start_time))

    os.system('rmdir /S /Q {}'.format(clone_dir))
    start_time = timeit.default_timer()
    os.system('git clone {} {}'.format(os.path.join(os.getcwd() + '\\practice_python'), clone_dir))
    print('completed in {}'.format(timeit.default_timer() - start_time))

    os.system('rmdir /S /Q {}'.format(clone_dir))
    start_time = timeit.default_timer()
    os.system('git clone --depth 1 file://{} {}'.format(os.path.join(os.getcwd() + '\\practice_python'), clone_dir))
    print('completed in {}'.format(timeit.default_timer() - start_time))

    """
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

    for k in range(97, 1000):
        if k:
            os.system('rmdir /S /Q "tmp_git_repo_clone{}"'.format(k - 1))
        os.chdir('tmp_git_repo_clone{}'.format(k))
        os.system('git pull --rebase')
        os.system('git push')
        os.chdir('..')
    """
