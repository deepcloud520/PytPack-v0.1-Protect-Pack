import os,zlib,time,sys
import py_compile as comp
'''
take a pack-python code
made by deepcloud
ver 0.1
Can run!!!
'''
PYTHON_RUN_COMMAND='python3 '   #the run command
logo=r'''
+-----------------------------------------------------+
|  ____        _   ____            _       ___   _    |
| |  _ \ _   _| |_|  _ \ __ _  ___| | __  / _ \ / |   |
| | |_) | | | | __| |_) / _` |/ __| |/ / | | | || |   |
| |  __/| |_| | |_|  __/ (_| | (__|   <  | |_| || |   |
| |_|    \__, |\__|_|   \__,_|\___|_|\_\  \___(_)_|   |
|        |___/                                        |
|                          by Deep_cloud              |
+-----------------------------------------------------+
'''
tem=r'''
print('Running PytPack\n')
f=open('temp__FILE','wb')
d=zlib.decompress(DATA)
f.write(d)
f.close()
os.system('PYTHON'+os.getcwd()+'/temp__FILE')
os.remove(os.getcwd()+'/temp__FILE')
'''
def cls_prt(strs):
    sys.stdout.write(strs + '\r')
    sys.stdout.flush()
def make_pack(infile,outfile):
    jd=0
    fs=None
    data=''
    info='complieing'
    for jd in range(100):#the cool display!!
        time.sleep(0.03)
        if jd==20:
            new=infile.replace('.py','.pyc')
            comp.compile(infile,new)
            infile=new
        elif jd==50:
            info='read the data'
            fs=open(infile,mode='rb')
            data=fs.read()#read the non-compress data
            fs.close()
        elif jd==90:
            info='ready to make pack'
            fs=open(outfile,mode='wb')
            data=zlib.compress(data,9)#.decode('utf-8')#compress the data
        elif jd==99:#write the unpack data code
            # the spaces are to fill last data
            info='making pack              '
            fs.write(b'import os,zlib,sys\n')
            fs.write(tem.replace('FILE',outfile).replace('DATA',str(data)).replace('PYTHON',PYTHON_RUN_COMMAND).encode('utf-8'))
        cls_prt('making pack python '+outfile+'....'+str(jd)+'%:'+info)
    fs.close()
    os.remove(infile)
    '''
    fs=open(infile,mode='r')
    l=len(fs.read())
    fs.close()
    fs=open(outfile,mode='r')
    l=l-len(fs.read())
    fs.close()
    '''
    cls_prt('Complete!                                       ')
    time.sleep(3)
def de_pack(infile,outfile): #decompress the pack file
    fs=open(infile,mode='r')
    infile_lst=fs.readlines()
    fs.close()
    cls_prt('De pack '+infile + '...read data')
    fs=open('__DEPACK__'+infile,mode='wb')
    fs.write(infile_lst[0].encode('utf-8'))
    fs.write(infile_lst[4].encode('utf-8'))
    fs.write(('f=open(\''+outfile+'\',mode=\'wb\')\nf.write(d)\nf.close()').encode('utf-8'))
    fs.close()
    cls_prt('De pack '+infile + '...start de-compress')
    os.system('python3 ' + os.getcwd()+'/__DEPACK__'+infile)
    os.remove(os.getcwd()+'/__DEPACK__'+infile)
    cls_prt('complete!                                      ')
def mainloop():#main loop
    print(logo)
    if len(sys.argv)>=3:
        if '-dP' not in sys.argv:
            make_pack(sys.argv[1],sys.argv[2])
        else:
            de_pack(sys.argv[1],sys.argv[2])
        return
    while True:
        try:
            cls_prt('Plese input filename:')
            infile=input()
            cls_prt('Plese input pack-filename:')
            outfile=input()
            make_pack(infile,outfile)
        except KeyboardInterrupt:
            cls_prt('Thanks for you use PytPack!')
            return

mainloop()