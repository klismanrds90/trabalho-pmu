import ctypes
import sqlite3
from PyQt5 import uic, QtWidgets

class Formulario(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("formulario.ui", self)

        self.botao_1.clicked.connect(self.limpar)
        self.botao_2.clicked.connect(self.funcao_principal)

        self.horario.addItems([" ", "08:00", "09:00", "13:00", "14:00", "14:30", "14:40", "15:00", "16:00", "16:20", "18:00", "19:00"])
        self.cor.addItems([" ", "Branca", "Preta", "Parda", "Amarela", "Indigena"])
        self.sexo.addItems([" ", "Masculino", "Feminino", "Outros"])
        self.estadocivil.addItems([" ", "Solteiro(a)", "Casado(a)", "Separado(a)", "União Estável", "Viúvo(a)"])
        self.tmoradia.addItems([" ", "Natural", "Menos de 5 anos", "Mais de 5 anos"])
        self.escolaridade.addItems([" ", "Fundamental Completo", "Fundamental Incompleto", "Ensino Médio Completo", "Ensino Médio Incompleto", "Superior Incompleto", "Superior Completo"])
        self.situacao.addItems([" ", "Empregado", "Desempregado", "Inss", "Autônomo", "Auxílio", "Aposentado", "Estudante"])
        self.residencia.addItems([" ", "Própria", "Alugada", "Financiada", "Cedida"])
        self.observacao.addItems([" ", "TV", "Facebook", "Instagram", "WhatsApp", "Panfleto/ Folheto", "Amigos", "Outros"])

    def funcao_principal(self):
        curso = self.curso.text().title()
        horario = self.horario.currentText()
        datainicio = self.datainicio.text().title()
        nome = self.nome.text().title()
        datanasc = self.datanasc.text()
        idade = self.idade.text()
        cor = self.cor.currentText()
        sexo = self.sexo.currentText()
        estadocivil = self.estadocivil.currentText()
        filiacao = self.filiacao.text().title()
        naturalidade = self.naturalidade.text().title()
        uf = self.uf.text().upper()
        tmoradia = self.tmoradia.currentText()
        endereco = self.endereco.text().title()
        numero = self.numero.text().title()
        cep = self.cep.text()
        bairro = self.bairro.text().title()
        telefone1 = self.telefone1.text().title()
        telefone2 = self.telefone2.text().title()
        rg = self.rg.text().title()
        orgaoexp = self.orgaoexp.text().upper()
        dataemissao = self.dataemissao.text()
        cpf = self.cpf.text()
        deficiencia = self.deficiencia.text().title()
        escolaridade = self.escolaridade.currentText()
        situacao = self.situacao.currentText()
        renda = self.renda.text().title()
        nummoradores = self.nummoradores.text().title()
        rendamoradores = self.rendamoradores.text().title()
        residencia = self.residencia.currentText()
        valorresidencia = self.valorresidencia.text()
        numtrabalham = self.numtrabalham.text()
        observacao = self.observacao.currentText()
        datainscricao = self.datainscricao.text()
        fezcurso = self.fezcurso.text()
        email = self.email.text()

        if curso == "":
            self.show_message_box("PREENCHA O CURSO DESEJADO", "ATENÇÃO!")
        elif nome == "":
            self.show_message_box("PREENCHA O NOME DO ALUNO", "ATENÇÃO!")
        elif idade == "":
            self.show_message_box("PREENCHA IDADE", "ATENÇÃO!")
        elif telefone1 == "":
            self.show_message_box("PREENCHA O TELEFONE", "ATENÇÃO!")
        else:
            try:
                banco = sqlite3.connect('banco_cadastro.db')
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS dados (Curso text, Horario text, DataInicio text, fezcuro text, Email, Data_Inscricao, Nome text, datanasc text, Idade text, Cor text, Sexo text, Estadocivil text, Filiacao text, Naturalidade text, Uf text, Tempomoradia text, Endereco text, Num text, Cep text, Bairro text, Telefone1 text, Telefone2 text, Rg text, OrgaoEmissor text, DataEmissao text, Cpf text, Deficiencia text, Escolaridade text, Situacao text, Renda text, NumMoradores text, numtrabalham text, RendaTotal text, Residencia text, ValorResidencia text, observacao text)",
                            )
                cursor.execute("INSERT INTO dados VALUES ('"+curso+"','"+horario+"','"+datainicio+"','"+fezcurso+"','"+email+"','"+datainscricao+"', '"+nome+"', '"+datanasc+"', '"+idade+"', '"+cor+"', '"+sexo+"', '"+estadocivil+"', '"+filiacao+"', '"+naturalidade+"', '"+uf+"', '"+tmoradia+"', '"+endereco+"', '"+numero+"','"+cep+"', '"+bairro+"', '"+telefone1+"', '"+telefone2+"', '"+rg+"', '"+orgaoexp+"', '"+dataemissao+"', '"+cpf+"','"+deficiencia+"', '"+escolaridade+"','"+situacao+"','"+renda+"', '"+nummoradores+"','"+numtrabalham+"', '"+rendamoradores+"','"+residencia+"','"+valorresidencia+"','"+observacao+"')")

                banco.commit()
                self.clear_form()
                self.show_message_box("DADOS INSERIDOS COM SUCESSO!", "OBRIGADO!")
                banco.close()
            except(sqlite3.OperationalError):
                self.show_message_box("EXISTEM ALTERAÇÕES NO BANCO DE DADOS, POR FAVOR SALVE E FECHE E DEPOIS TENTE NOVAMENTE!", "ERRO!")

    def limpar(self):
        self.clear_form()
        self.show_message_box("DADOS LIMPOS!!", "SUCESSO!")

    def clear_form(self):
        self.curso.setText("")
        self.datainicio.setText("")
        self.fezcurso.setText("")
        self.email.setText("")
        self.datainscricao.setText("")
        self.nome.setText("")
        self.datanasc.setText("")
        self.idade.setText("")
        self.filiacao.setText("")
        self.naturalidade.setText("")
        self.uf.setText("")
        self.endereco.setText("")
        self.numero.setText("")
        self.cep.setText("")
        self.bairro.setText("")
        self.telefone1.setText("")
        self.telefone2.setText("")
        self.rg.setText("")
        self.orgaoexp.setText("")
        self.dataemissao.setText("")
        self.cpf.setText("")
        self.deficiencia.setText("")
        self.renda.setText("")
        self.nummoradores.setText("")
        self.rendamoradores.setText("")
        self.valorresidencia.setText("")
        self.numtrabalham.setText("")
        self.observacao.setCurrentIndex (0)
        self.horario.setCurrentIndex (0)
        self.cor.setCurrentIndex (0)
        self.sexo.setCurrentIndex (0)
        self.estadocivil.setCurrentIndex (0)
        self.tmoradia.setCurrentIndex (0)
        self.escolaridade.setCurrentIndex (0)
        self.situacao.setCurrentIndex (0)
        self.residencia.setCurrentIndex (0)

    def show_message_box(self, message, title):
        ctypes.windll.user32.MessageBoxW(0, message, title, 0)

app = QtWidgets.QApplication([])
formulario = Formulario()
formulario.show()
app.exec()
