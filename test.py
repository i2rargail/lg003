import threading
import os

def copyfile(srcpath,dstpath):
    with open(srcpath,'rb') as r:
        with open(dstpath,'wb') as w:
            w.write(r.read())


def copydir(src_dirpath,dst_dirpath):
    filelist=os.listdir(src_dirpath)
    if len(filelist)==0:
        if not os.path.exists(dst_dirpath):
            os.makedirs(dst_dirpath)
            return
    for i in filelist:
        srcpath=src_dirpath + '/' + i
        dstpath=dst_dirpath + '/' + i
        if os.path.isfile(srcpath):
            if not os.path.exists(dst_dirpath):
                os.makedirs(dst_dirpath)
            th1=threading.Thread(target=copyfile,args=(srcpath,dstpath))
            th1.start()
            th1.join()

        elif os.path.isdir(srcpath):
            copydir(srcpath,dstpath)

def main():
    src_dirpath=input('输入需要备份的文件路径:')
    if not os.path.exists(src_dirpath):
        print('输入有误...')
        return
    dst_dirpath=input('输入存放备份文件的位置:')
    th2=threading.Thread(target=copydir,args=(src_dirpath,dst_dirpath))
    th2.start()
    print("copy完成...")

if __name__=='__main__':
    main()
