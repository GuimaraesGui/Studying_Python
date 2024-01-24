import win32com.client as win32

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)
faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento / qtde_produtos

# configurar as informações do seu e-mail
email.To = "guimaraes_gui@outlook.com.br" #Ex:"destino; destino2"
email.Subject = "E-mail automático do Python" #Assunto
email.HTMLBody = f"""
<p>Olá Lira, aqui é o código Python</p>

<p>O faturamento da loja foi de R${faturamento}</p>
<p>Vendemos {qtde_produtos} produtos</p>
<p>O ticket Médio foi de R${ticket_medio}</p>

<p>Abs,</p>
<p>Código Python</p>
"""

anexo = anexo = "C:\\Users\\00805129\\OneDrive - NATURGY INFORMATICA S.A\\Documentos\\02 - Industrial\\Qualidade GNV\\CFQ - SPS\\01 - JANEIRO\\01 - Janeiro - 2024 - Média Composição do Gás Natural1.xlsx"
email.Attachments.Add(anexo)

email.send()
print("Email Enviado")