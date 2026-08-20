# Aula de Testes de Integração com pytest
 
Projeto prático da disciplina de Testes de Software.
 
## Objetivo
 
Praticar testes unitários, testes de integração,
valores-limite, parametrização e testes de exceção
usando Python e pytest.
 
## Regras do projeto
 
- O preço não pode ser negativo.
- O desconto deve estar entre 0% e 100%.
- A quantidade deve ser maior que zero.
- Subtotal abaixo de R$ 200,00 paga R$ 20,00 de frete.
- Subtotal igual ou superior a R$ 200,00 possui frete grátis.
 
## Conteúdos
 
- Testes unitários
- Testes de integração
- Arrange-Act-Assert
- Cenários de teste
- Valores-limite
- pytest.mark.parametrize
- pytest.raises
- Relatório HTML
 
## Instalação
 
python -m pip install -r requirements.txt
 
## Executar os testes
 
python -m pytest -v
 
## Gerar o relatório
 
python -m pytest -v --html=relatorio_testes.html --self-contained-html

