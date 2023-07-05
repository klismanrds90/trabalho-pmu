# Mensagem para o usuário fechar o banco de dados antes de realizar o backup
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show('REALIZANDO BACKUP, POR FAVOR FECHE O BANCO DE DADOS E DEPOIS CLIQUE EM OK.', 'BACKUP BANCO DE DADOS', 'OK', 'Warning')

# Definindo os caminhos dos arquivos e diretórios
$pastaOrigem = "C:\Inscricao 2023\banco_cadastro.db"
$pastaDestino = "E:\Backup_BD"

# Realizando a cópia do arquivo de backup com condição try para erros
try {
    $dataAtual = Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'
    $arquivoDestino = Join-Path -Path $pastaDestino -ChildPath "banco_cadastro_$dataAtual.db"
    Copy-Item -Path $pastaOrigem -Destination $arquivoDestino -Force -Verbose
}
catch {
    # Mensagem de erro em caso de falha na cópia
    Add-Type -AssemblyName System.Windows.Forms
    [System.Windows.Forms.MessageBox]::Show("Ocorreu um erro ao realizar o backup: $_", 'ERRO', 'OK', 'Error')
    exit 1
}

# Renomeando o arquivo copiado com a data e hora atual
$newName = "banco_cadastro_$dataAtual.db"
Rename-Item -Path $arquivoDestino -NewName $newName


# Mensagem de conclusão do processo
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show('Processo finalizado!!', 'CONCLUIDO', 'OK', 'Warning')

# Excluindo arquivos com mais de 10 dias
$limiteDias = -10
Get-ChildItem $pastaDestino | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays($limiteDias) } | Remove-Item -Force -Verbose
