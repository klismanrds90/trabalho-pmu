# Script para Backup de Banco de Dados
Descrição
Este script em PowerShell realiza o backup de um banco de dados SQLite localizado em uma pasta específica. O script copia o arquivo do banco de dados para uma pasta de destino e adiciona 
a data e hora atual ao nome do arquivo copiado. Além disso, o script também exclui automaticamente os backups antigos que têm mais de 10 dias na pasta de destino.

# Funcionamento do Script
Após configurar uma tarefa rotineira no windows para executar o backup 2 vezes ao dia,
O script exibirá uma mensagem para o usuário, solicitando que ele feche o banco de dados antes de realizar o backup.
O script definirá os caminhos da pasta de origem do banco de dados ($pastaOrigem) e da pasta de destino para o backup ($pastaDestino).
Será obtida a data e hora atual para nomear o arquivo de backup com o formato "banco_cadastro_yyyy-MM-dd_HH-mm-ss.db".
O arquivo de backup será copiado da pasta de origem para a pasta de destino usando o cmdlet Copy-Item.
Em caso de sucesso, uma mensagem de conclusão será exibida ao usuário.
Em caso de falha na cópia, uma mensagem de erro será exibida ao usuário com detalhes do erro.
O script verifica os backups antigos na pasta de destino e exclui automaticamente os arquivos que têm mais de 10 dias, usando o cmdlet Get-ChildItem e Remove-Item.

# Observações
O script foi projetado para fazer backup de arquivos SQLite, como mencionado na variável $pastaOrigem.
Habilitada a execução de scripts do PowerShell em cada máquina. Podemos habilitar a execução de scripts do PowerShell digitando Set-ExecutionPolicy RemoteSigned em um prompt do PowerShell com privilégios de administrador.
