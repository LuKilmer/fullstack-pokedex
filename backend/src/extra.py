class TColor:
    '''Terminal Colorido'''
    @staticmethod
    def resetarCor():
        return "\033[0;0m" 

    @staticmethod
    def corRosa():
        return "\033[1;35m"
    
    @staticmethod
    def corRoxo():
        return "\033[0;35m"
    
    @staticmethod
    def corBold():
        return "\033[;1m"
    
    @staticmethod
    def corReverso():
        return "\033[;7m"
    
    @staticmethod
    def corVermelha():
        return "\033[1;31m"
    
    @staticmethod
    def corAzul():
        return "\033[1;34m"  
    
    @staticmethod
    def corCiano():
        return "\033[1;36m" 
    
    @staticmethod
    def corVerde():
        return "\033[1;32m" 
    
    @staticmethod
    def corAmarela():
        return "\033[1;33m"
    
    @staticmethod
    def corAzul():
        return "\033[1;34m" 
