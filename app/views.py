from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request,'inicio.html')

def index(request):
    return render(request,'index.html')

def imc(request):
    '''
    FUNÇÃO RESPONSAVÉL PELO TRATAMENTO DE ERRO
    EXIBIÇÃO DO CONTEÚDO NO HTML
       '''
    if request.method == 'POST':
    
        try:
            peso = float(request.POST.get('peso', 0))
            altura = float(request.POST.get('altura', 0))
            resultado = calcular(peso,altura)
            return render(request,'index.html', {'resultado': round(resultado,2)})
        
        except:
            erro = mensagemerro()
            return (render (request, 'index.html', {'erro':erro}))


def mensagemerro():
    '''FUNÇÃO RESPONSAVEL POR EXIBIR A MENSAGEM DE ERRO '''
    texto = (f'VALORES INVÁLIDOS!')
    return texto

def indice(resultado):
    ''' FUNÇÃO RESPONSAVÉL DE CLASSIFICAR E INFORMAR O GRAU DE OBESIDADE DO USUARIO BASEADO NO SEU IMC '''
    grau = 0
    classe = None

    if resultado < 18.5:
        grau = 0        
        classe = 'Magreza'

    elif resultado >= 18.5 and resultado <= 24.9:
        grau = 0
        classe = 'Normal'

    elif resultado >=25.0 and resultado <= 29.9:
        grau = 1 
        classe = 'Sobrepeso'

    elif resultado >= 30 and resultado <= 39.9:
        grau = 2
        classe = 'Obesidade'

    elif resultado >= 40:
        grau = 3
        classe = 'Obesidade Grave'

    else:
        return grau, classe

def calcular(peso,altura):
    '''FUNÇÃO RESPONSAVEL POR 
    CALCULAR O IMC
    VERIFICAR O PESO E A ALTURA DO USUARIO CASO SEJA DESPROPORCIONAL
    '''
    altura = altura / 100
    # peso = peso / 100

    verifica_peso = peso > 150 or peso < 2
    verifica_altura = altura > 2.30 or altura < 0.70

    if verifica_peso == True:
        return mensagemerro()
    
    elif verifica_altura == True:
        return mensagemerro()
     
    else:
        return peso / (altura * altura)