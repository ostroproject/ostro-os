import ConfigParser
import os

class ReadConfFile:
    currentDir=os.path.dirname(__file__) 
    filepath=currentDir+os.path.sep+"/SensorConfig.ini"
    print filepath;
    @staticmethod
    def getConfigParser():
        cf=ConfigParser.ConfigParser()
        cf.read(ReadConfFile.filepath)
        return cf

    @staticmethod
    def getSectionValue(section,key):
        cf=ReadConfFile.getConfigParser()
        return cf.get(section, key)
    
if __name__ == '__main__':
    x=ReadConfFile.getSectionValue( 'sensors','valid-id')
    print x
