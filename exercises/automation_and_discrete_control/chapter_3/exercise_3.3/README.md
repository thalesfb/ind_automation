### 3.3)
Elaborar um programa PLC capaz de efetuar controle de uma prensa que é manejada por dois operários. Cada um deles utiliza um atuador que exige o emprego de ambas as mãos. A operação de prensagem realiza-se quando se põe em marcha um motor que está comandado pelo contactor R. Por razões de segurança dos operários, foi decidida a seguinte sequência de funcionamento:

1. Com somente um operador, não se pode ativar a prensa;

2. Com os dois operários atuando nos comandos A e B, a prensa abaixa;

3. Se atua um operário, mas o outro tarda mais do que três segundos, a prensa não deve operar, e é necessário repetir a manobra;

4. Se ativado o contactor R e um qualquer dos operários retirar as mãos do contato, R desativa e não volta a se ativar se o operário demorar mais do que três segundos para recolocar suas mãos no contato, caso em que deverá repetir-se a manobra por ambos os operários.