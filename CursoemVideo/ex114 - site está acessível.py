import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:   # except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())   # com isso eu posso conseguir o código do site
