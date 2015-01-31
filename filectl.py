# -*- coding: utf-8 -*-
'''
File Name: filectl
Created on 2015年1月31日 上午11:55:18

@author: jay
'''
import binascii,time
class FileCtl():
    def Open(self,filename,opt='rb'):
        try:
            self.filename=filename
            self.fp=open(self.filename,opt)  ####we have to use rb mode
        except:
            print 'Open file %s failed'%self.filename
            return False
        return True
    
    def Close(self):
        try:
            self.fp.close()
            self.fp=None
        except:
            print 'Close file %s failed'%self.filename
            return False
        return True
    
    def Read(self):
        readlen=0
        while readlen<10:
            #lastaddr=self.fp.tell()
            tmp=self.fp.readline()    ####include  0A or OD
            tmp=tmp.strip('\r\n')
            print tmp 
            readlen+=1
    
    def ReadOneSentence(self):
        try:
            tmp=self.fp.readline()    ####include  0A or OD
        except :
            return False
        
        if not tmp:
            #print "EOFFFFFFFFFFFF"
            return False
        
        tmp=tmp.strip('\r\n')
        if tmp[-1] != '|':
            print "read wrong:",tmp
            return False
        src=tmp
        
        tmp=self.fp.readline()    ####include  0A or OD
        tmp=tmp.strip('\r\n')
        if tmp[-1] != '|':
            print "read wrong:",tmp
            return False
        tra=tmp
        
        tmp=self.fp.readline()    ####include  0A or OD
        tmp=tmp.strip('\r\n')   
        if tmp[0] != '~':
            print "wrong ~",tmp
            return False
        return True,src,tra     
    def WriteOneSentence(self,src,tra):
        self.fp.writelines(src+"\n")
        self.fp.writelines(tra+"\n")
        self.fp.writelines("~\n")
        
    def FindTranslate(self,filename,msg):
        if not self.Open(filename):
            return False
        
        ###read ef bb 
        buf=self.fp.read(3)
        if buf=='\xef\xbb\xbf':
            pass#print 'itis utf-8'
        else:
            self.fp.seek(0)
        
        while True:
            ret=self.ReadOneSentence()
            if not ret:
                self.Close()
                return False
            else:
                if msg==ret[1]:
                    #print "Find It!",ret[2]
                    self.Close()
                    return True,ret[2]
            
    def selftest(self):
        if not self.Open("Translate.txt"):
            return False
        
        ret,src,tra=self.ReadOneSentence()
        if not ret:
            print 'read error'
        else:
            print src
            print tra
        self.Close()
        
def selftest():
    fs=FileCtl()
    fout=FileCtl()

    #fs.selftest()
    if not fs.Open("Translatesrc.TXT"):
        exit(1)

    newfile="Translate"+time.strftime("%m%d%H%M%S")+".txt"
    if not fout.Open(newfile,opt='w'):
        exit(1)
        
    while True:
        ret=fs.ReadOneSentence()
        if not ret:
            print "Read End"
            break
        src=ret[1]
        
        buf=FileCtl().FindTranslate("Translateref.TXT",src)
        if not buf:
            tra="|"
        else:
            tra=buf[1]
        fout.WriteOneSentence(src, tra)
        
    print "Translate Success to file ",newfile
    fout.Close()
    fs.Close()
if __name__ == '__main__':
    pass
    print time.strftime("%m%d%H%M%S")
    selftest()
    