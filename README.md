# 

<h1 align="center">
  <br>
    <img width="200px" src="https://github.com/Ukobir/pwmControl/blob/main/imagens/logo.png">
  <br>
    MPU Data Recorder
  <br>
</h1>

## Descrição

O objetivo deste projeto é desenvolver uma ferramenta capaz de capturar os dados de aceleração e giroscópio ao usar o sensor MPU6050 e guardar em um cartão micro SD. Para isto, foi utilizado a placa Bitdoglab que possui as conectividades necessárias e, além disso, possui componentes físicos que auxiliam o usuário, como: display, botões, buzinas, etc.

### Pré-requisitos

1. **Git**: Certifique-se de ter o Git instalado no seu sistema. 
2. **VS Code**: Instale o Visual Studio Code, um editor de código recomendado para desenvolvimento com o Raspberry Pi Pico.
3. **Pico SDK**: Baixe e configure o SDK do Raspberry Pi Pico, conforme as instruções da documentação oficial.
4. Tenha acesso a placa **Bitdoglab**.

### Passos para Execução

1. **Clonar o repositório**: Clone o repositório utilizando o comando Git no terminal:
   
   ```bash
   https://github.com/Ukobir/MPU-Data-Recorder
   ```
2. Importar o código no VS Code com a extensão do Raspberry pi pico.
3. Compilar o código e carregar o código na **BitDogLab**.

##
Estes dados de aceleração e giroscópio estão no formato CSV e podem ser utilizados no código em Python que está também disponível, informa as 50 primeiras amostras. 
O código .py está disponível na pasta ArquivosDados.

## Testes Realizados
Foi feito diversos testes para garantir a funcionamento devido da atividade. Além de que foi organizado o código conforme explicado em aula.

## Vídeo de Demonstração
[Link do Vídeo](https://drive.google.com/file/d/1mzyJ4G52h0fkXQPf_OVL8cpS8XzI0cUQ/view?usp=sharing)


