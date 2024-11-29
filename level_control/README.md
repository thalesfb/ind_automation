# ETE - Processo de Fabricação de Papel

## 1. Introdução

A indústria papeleira desempenha um papel importante na economia, especialmente na região do meio oeste catarinense, onde a atividade está profundamente ligada ao desenvolvimento econômico local e à geração de empregos. O processo de fabricação de papel consome uma quantidade significativa de água em várias etapas, desde a preparação da polpa até o tratamento de resíduos, o que torna o gerenciamento eficiente desse recurso um ponto crucial para a sustentabilidade e competitividade da indústria.

No processo principal de fabricação, a água é utilizada de maneira intensiva e, ao longo das diversas etapas, grande parte dessa água é recuperada e reciclada. No entanto, a eficiência desse reaproveitamento depende diretamente de um controle preciso e de processos bem gerenciados de tratamento da água excedente. Neste contexto, o tratamento de água desempenha um papel fundamental, pois permite não apenas o reaproveitamento, mas também a melhoria da qualidade da água e a recuperação de fibras, aumentando a eficiência e reduzindo os impactos ambientais.

### 1.1. Justificativa

O tratamento de água na indústria de papel é crítico tanto pela importância da água no processo quanto pela necessidade de práticas sustentáveis que reduzam o impacto ambiental. Sem automação e controle adequados, há uma perda significativa de água e fibras, o que acarreta aumento nos custos de produção e consumo de recursos naturais.

A analogia com a falta de automação é clara: imagine que, sem um controle preciso, a quantidade de fibras de papel que poderia ser recuperada e reinserida no processo é perdida para o efluente, representando um custo oculto, mas significativo. O tratamento manual, sem a devida automação, também pode resultar em variações na qualidade da água tratada, afetando as etapas seguintes de produção e a consistência do produto final.

### 1.2. Problema

O problema central reside na ausência de automação adequada do processo de tratamento de água, que atualmente é realizado de forma manual. Isso resulta em uma série de desafios operacionais, como:

- **Perda de Recursos**: Fibras de papel que poderiam ser recuperadas são frequentemente descartadas, aumentando os custos de matéria-prima.
- **Ineficiência no Uso de Água**: A falta de controle sobre os níveis de água, bem como a dosagem de produtos químicos, leva ao desperdício, aumentando o consumo de água e afetando a eficiência da operação.
- **Qualidade Inconsistente**: O controle manual também implica em variações na dosagem de coagulantes e polímeros, o que pode afetar a qualidade da água tratada e o desempenho do processo produtivo como um todo.

### 1.3. Objetivo

O objetivo deste documento é descrever o subprocesso de tratamento de água utilizado no processo principal de fabricação de papel e propor a implementação de automação para otimizar o uso da água e a recuperação de fibras. Com a automação, busca-se alcançar maior eficiência e sustentabilidade, minimizando desperdícios e melhorando a consistência e a qualidade do processo.

### 1.4. Escopo

O escopo do projeto abrange a análise detalhada dos equipamentos e processos envolvidos no tratamento da água excedente, com foco na otimização através de técnicas de controle e automação. Será elaborado um plano para implementação de sensores e sistemas automatizados para monitoramento dos níveis de água e dosagem dos produtos químicos, além de sistemas de alarme e segurança que garantam a operação dentro dos parâmetros desejados.

## 2. Diagramação

O diagrama a seguir ilustra o subprocesso de tratamento de água no processo de fabricação de papel, destacando os equipamentos envolvidos e o fluxo operacional, incluindo os tanques de polímero e coagulante que dosam diretamente no flotador.

```mermaid
graph TD;
    TK-101[Tanque Principal] --> P-101[Bomba];
    P-101 --> TK-102[Tanque Secundário];
    TK-102 --> P-102-A[Bomba];
    TK-102 --> P-102-B[Bomba];
    P-102-A -->|Fluxo calculado| F[Flotador];
    P-102-B -->|Fluxo calculado| F[Flotador];

    P-103 -->|Dosagem Automática| F;
    P-104 -->|Dosagem Automática| F;

    subgraph Água
      F -->|Água| TK-105[Tanque Água];
      P-105[Bomba] -->|Água| TK-105;
    end
    subgraph Fibras
      F -->|Fibras| TK-106[Tanque Fibras];
      TK-106 -->|Fibras| P-106[Bomba];
    end

    subgraph Químicos
      TK-201[Tanque d'água] --> TK-104-A[Tanque de Polímero A];
      TK-201 --> TK-104-B[Tanque de Polímero B];
      TK-201 --> TK-103-A[Tanque de Coagulante A];
      TK-201 --> TK-103-B[Tanque de Coagulante B];
      subgraph Polímeros
         TK-104-A --> S[Seleção];
         TK-104-B --> S[Seleção];
         S --> P-104[Dosagem];
      end
      subgraph Coagulantes
         TK-103-A --> S2[Seleção];
         TK-103-B --> S2[Seleção];
         S2 --> P-103[Dosagem];
      end
    end
```

## 3. Equipamentos Envolvidos

### 3.1. Tanque Principal (Tanque 1)

- **Função**: Capta toda a água excedente utilizada no processo de fabricação de papel.
- **Capacidade**: 80 metros cúbicos.
- **Bombeamento**: Realizado por uma bomba sapo com capacidade de 100 metros cúbicos por hora.
- **Transporte**: A água do Tanque Principal é transportada para o Tanque Secundário.

### 3.2. Tanque Secundário (Tanque 2)

- **Função**: Recebe a água do Tanque Principal e alimenta o flotador.
- **Capacidade**: 36 metros cúbicos.
- **Bombeamento**: Duas bombas de 20 cavalos, cada uma fornecendo 100 metros cúbicos de água por hora.
- **Transporte**: A água do Tanque Secundário é bombeada para o flotador.

### 3.3. Flotador

- **Função**: Realiza a flotação das fibras de papel da água e arrasta as fibras para recuperação e a água para reaproveitamento.
- **Capacidade**: 100 metros cúbicos por hora.
- **Produtos Químicos**: São aplicados para auxiliar na separação das fibras de papel.
- **Destino da Água**: Após o tratamento, a água segue para o Tanque Terciário.

### 3.4. Tanque Terciário (Tanque 3)

- **Função**: Armazena a água tratada do Flotador e retroalimenta o processo, evitando a dispersão e permitindo o reaproveitamento da água.
- **Capacidade**: 40 metros cúbicos.
- **Bombeamento**: Realizado por uma bomba de 1 cavalo.
- **Abastecimento**: Alimentado pela água tratada do Flotador.

### 3.5. Tanque de Polímero 1 (Tanque 4)

- **Função**: Armazena o polímero catiônico utilizado no tratamento de água.
- **Capacidade**: 1,8 metros cúbicos.
- **Bombeamento**: Realizado por uma bomba de 1 cavalo.
- **Abastecimento**: Registro de água para diluição do polímero catiônico antes da aplicação no flotador.
- **Válvula de Saída**: Válvula de controle para dosagem do polímero no flotador.
- **Dosagem**: O polímero é dosado no flotador para auxiliar na separação das fibras de papel.

### 3.6. Tanque de Polímero 2 (Tanque 5)

- **Função**: Armazena o polímero catiônico utilizado no tratamento de água.
- **Capacidade**: 1,8 metros cúbicos.
- **Bombeamento**: Realizado por uma bomba de 1 cavalo.
- **Abastecimento**: Registro de água para diluição do polímero catiônico antes da aplicação no flotador.
- **Válvula de Saída**: Válvula de controle para dosagem do polímero no flotador
- **Dosagem**: O polímero é dosado no flotador para auxiliar na separação das fibras de papel.

### 3.7. Tanque de Coagulante (Tanque 6)

- **Função**: Armazena o coagulante utilizado no tratamento de água.
- **Capacidade**: 1,2 metros cúbicos.
- **Bombeamento**: Realizado por uma bomba de 1 cavalo.
- **Abastecimento**: Registro de água para diluição do coagulante antes da aplicação no flotador.
- **Válvula de Saída**: Válvula de controle para dosagem do coagulante no flotador
- **Dosagem**: O coagulante é dosado no flotador para auxiliar na separação das fibras de papel.

### 3.8. Tanque de Coagulante 2 (Tanque 7)

- **Função**: Armazena o coagulante utilizado no tratamento de água.
- **Capacidade**: 1,2 metros cúbicos.
- **Bombeamento**: Realizado por uma bomba de 1 cavalo.
- **Abastecimento**: Registro de água para diluição do coagulante antes da aplicação no flotador.
- **Válvula de Saída**: Válvula de controle para dosagem do coagulante no flotador
- **Dosagem**: O coagulante é dosado no flotador para auxiliar na separação das fibras de papel.

## 4. Fluxo Operacional

1. A água excedente utilizada no processo principal de fabricação de papel é direcionada ao Tanque Principal.
2. A bomba sapo do Tanque Principal transporta a água para o Tanque Secundário.
3. No Tanque Secundário, uma das bombas abastece o flotador.
4. É aplicado um coagulante para auxiliar na flotação das fibras de papel.
5. É preparado e aplicado um polímero catiônico para aplicação no flotador, auxiliando na separação das fibras de papel.
6. No flotador, produtos químicos são aplicados para separar as fibras de papel da água. O operador ajusta manualmente a vazão de água e a quantidade de produtos químicos.
7. O Tanque Terciário retroalimenta o processo, reutilizando quase toda a água, reduzindo o desperdício.

## 5. Controle

O controle preciso dos níveis de água é crucial para evitar excesso ou escassez no sistema. É necessário equilibrar a quantidade de água consumida no processo de fabricação com a quantidade recuperada pelo flotador e armazenada nos tanques, sendo necessário monitorar a qualidade da água e a eficiência do tratamento. A aplicação dos produtos químicos deve ser ajustada conforme a necessidade, evitando excesso ou falta de produtos.

- **Tanque 1**: O nível deve ser mantido em 50% de sua capacidade para evitar transbordamento e garantir que a água seja bombeada para o Tanque 2.
- **Tanque 2**: Deve estar sempre em 100% de capacidade para garantir o abastecimento do flotador. Um medidor de fluxo na tubulação de saída deve ser monitorado para garantir a dosagem proporcional de produtos químicos.
- **Flotador**: Um sensor de nível deve ser monitorado para ativar ou desligar o equipamento conforme a necessidade.
- **Tanque 3**: O nível deve ser monitorado para garantir que a água seja direcionada para o processo de fabricação de papel. Se o nível estiver abaixo de 10%, a bomba principal deve ser acionada para bombear para o Tanque 3. Se o nível estiver acima de 90%, a bomba principal deve ser desligada para evitar transbordamento.

## 6. Lista de Materiais Necessários

1. **Bombas de Água**

   - 1 Bomba sapo (capacidade: 100 m³/h)
   - 2 Bombas de 20 cavalos (capacidade: 100 m³/h cada)
   - 1 Bomba de 1 cavalo para tanques de polímero
   - 1 Bomba de 1 cavalo para tanques de coagulante
   - 1 Bomba de 10 cavalos para a captação de água do rio para eventuais faltas de água no tanque terciário

2. **Tanques de Armazenamento**

   - Tanque Principal (80 m³)
   - Tanque Secundário (36 m³)
   - Tanque Terciário (40 m³)
   - Tanques de Polímero (2 tanques de 1,8 m³)
   - Tanques de Coagulante (2 tanques de 1,2 m³)

3. **Sensores e Medidores**

   - Sensores de nível (Tanque 1, Tanque 2, Flotador, Tanque 3)
   - Medidores de fluxo para monitoramento da saída do Tanque 2

4. **Produtos Químicos**

   - Coagulante para flotação
   - Polímero catiônico para separação de fibras

5. **Tubulações e Válvulas**

   - Tubulações para transporte de água entre os tanques
   - Válvulas para controle de abastecimento e dosagem de produtos químicos

6. **Sistemas de Controle e Automação**

   - Controladore lógico programávei (CLP) - Wago 750-8208
   - Alarmes visuais e sonoros para monitoramento de níveis como sirenes e luzes de alerta

7. **Licenças e Certificações**

   - Licença para o software e!Cockpit da Wago
   - Licença para o elipse E3 para monitoramento e controle

## 7. Mapeamento de Entradas, Saídas e Memórias

| **Tipo**              | **Endereço** | **Descrição**                                                     | **Símbolo**                |
| --------------------- | ------------ | ----------------------------------------------------------------- | -------------------------- |
| **Entradas Digitais** | `%I0.0`      | Sensor de nível muito alto no tanque TK-101                       | `INPUT_LTHH_TK101`         |
|                       | `%I0.1`      | Sensor de nível alto no tanque TK-101                             | `INPUT_LTH_TK101`          |
|                       | `%I0.2`      | Sensor de nível muito baixo no tanque TK-101                      | `INPUT_LTLL_TK101`         |
|                       | `%I0.2`      | Sensor de nível muito alto no tanque TK-103/A                     | `INPUT_LTHH_TK103_A`       |
|                       | `%I0.3`      | Sensor de nível muito baixo no tanque TK-103/A                    | `INPUT_LTLL_TK103_A`       |
|                       | `%I0.4`      | Sensor de nível muito alto no tanque TK-103/B                     | `INPUT_LTHH_TK103_B`       |
|                       | `%I0.5`      | Sensor de nível muito baixo no tanque TK-103/B                    | `INPUT_LTLL_TK103_B`       |
|                       | `%I0.6`      | Sensor de nível muito alto no tanque TK-104/A                     | `INPUT_LTHH_TK104_A`       |
|                       | `%I0.7`      | Sensor de nível muito baixo no tanque TK-104/A                    | `INPUT_LTLL_TK104_A`       |
|                       | `%I1.0`      | Sensor de nível muito alto no tanque TK-104/B                     | `INPUT_LTHH_TK104_B`       |
|                       | `%I1.1`      | Sensor de nível muito baixo no tanque TK-104/B                    | `INPUT_LTLL_TK104_B`       |
|                       | `%I1.2`      | Sensor de nível muito alto no tanque TK-105                       | `INPUT_LTHH_TK105`         |
|                       | `%I1.3`      | Sensor de nível muito baixo no tanque TK-105                      | `INPUT_LTLL_TK105`         |
|                       | `%I1.4`      | Botão Start do sistema                                            | `INPUT_START_BUTTON`       |
|                       | `%I1.5`      | Botão Stop do sistema                                             | `INPUT_STOP_BUTTON`        |
|                       | `%I1.6`      | Falha na bomba P-101A                                             | `INPUT_FAULT_P101A`        |
|                       | `%I1.7`      | Falha na bomba P-101B                                             | `INPUT_FAULT_P101B`        |
| **Saídas Digitais**   | `%Q0.0`      | Acionamento da bomba P-101 para abastecimento do TK-102           | `OUTPUT_RUN_P101`          |
|                       | `%Q0.2`      | Acionamento da bomba P-102/A                                      | `OUTPUT_RUN_P102A`         |
|                       | `%Q0.3`      | Acionamento da bomba P-102/B                                      | `OUTPUT_RUN_P102B`         |
|                       | `%Q0.4`      | Acionamento da bomba P-105 de água fresca                         | `OUTPUT_RUN_P103`          |
|                       | `%Q0.5`      | Acionamento da bomba P-103 da dosagem do coagulante               | `OUTPUT_RUN_P104`          |
|                       | `%Q0.6`      | Acionamento da bomba P-104 da dosagem do polímero                 | `OUTPUT_RUN_P105`          |
|                       | `%Q0.7`      | Acionamento do flotador                                           | `OUTPUT_RUN_FLOAT`         |
|                       | `%Q0.8`      | Alarme sonoro                                                     | `OUTPUT_ALARM`             |
|                       | `%Q0.9`      | Agitador do TK-103/A                                              | `OUTPUT_RUN_AGT_TK103_A`   |
|                       | `%Q0.10`     | Agitador do TK-103/B                                              | `OUTPUT_RUN_AGT_TK103_B`   |
|                       | `%Q0.11`     | Agitador do TK-104/A                                              | `OUTPUT_RUN_AGT_TK104_A`   |
|                       | `%Q0.12`     | Agitador do TK-104/B                                              | `OUTPUT_RUN_AGT_TK104_B`   |
|                       | `%Q0.13`     | Abertura da válvula pneumática para entrada de água do TK-103/A   | `OUTPUT_OPEN_VLV_TK103_A`  |
|                       | `%Q0.14`     | Abertura da válvula pneumática para entrada de água do TK-103/B   | `OUTPUT_OPEN_VLV_TK103_B`  |
|                       | `%Q0.15`     | Abertura da válvula pneumática para entrada de água do TK-104/A   | `OUTPUT_OPEN_VLV_TK104_A`  |
|                       | `%Q1.0`      | Abertura da válvula pneumática para entrada de água do TK-104/B   | `OUTPUT_OPEN_VLV_TK104_B`  |
|                       | `%Q1.1`      | Fechamento da válvula pneumática para entrada de água do TK-103/A | `OUTPUT_CLOSE_VLV_TK103_A` |
|                       | `%Q1.2`      | Fechamento da válvula pneumática para entrada de água do TK-103/B | `OUTPUT_CLOSE_VLV_TK103_B` |
|                       | `%Q1.3`      | Fechamento da válvula pneumática para entrada de água do TK-104/A | `OUTPUT_CLOSE_VLV_TK104_A` |
|                       | `%Q1.4`      | Fechamento da válvula pneumática para entrada de água do TK-104/B | `OUTPUT_CLOSE_VLV_TK104_B` |
| **Memórias Internas** | `%M0`        | Sensor de leitura de nível em 80% do TK-101                       | `INPUT_SENS_S1_TK-101`     |
|                       | `%M1`        | Sensor de leitura de nível em 50% do TK-101                       | `INPUT_SENS_S2_TK-101`     |
|                       | `%M2`        | Sensor de leitura de nível em 20% do TK-101                       | `INPUT_SENS_S3_TK-101`     |
|                       | `%M3`        | Sensor de leitura de nível alto do tanque TK-103/A                | `INPUT_SENS_SH_TK-103_A`   |
|                       | `%M4`        | Sensor de leitura de nível baixo do tanque TK-103/A               | `INPUT_SENS_SL_TK-103_A`   |
|                       | `%M5`        | Sensor de leitura de nível alto do tanque TK-103/B                | `INPUT_SENS_SH_TK-103_B`   |
|                       | `%M6`        | Sensor de leitura de nível baixo do tanque TK-103/B               | `INPUT_SENS_SL_TK-103_B`   |
|                       | `%M7`        | Sensor de leitura de nível alto do tanque TK-104/A                | `INPUT_SENS_SH_TK-104_A`   |
|                       | `%M8`        | Sensor de leitura de nível baixo do tanque TK-104/A               | `INPUT_SENS_SL_TK-104_A`   |
|                       | `%M9`        | Sensor de leitura de nível alto do tanque TK-104/B                | `INPUT_SENS_SH_TK-104_B`   |
|                       | `%M10`       | Sensor de leitura de nível baixo do tanque TK-104/B               | `INPUT_SENS_SL_TK-104_B`   |
|                       | `%M11`       | Sensor de leitura de nível alto do tanque TK-106                  | `INPUT_SENS_SH_TK-106`     |
|                       | `%M12`       | Sensor de leitura de nível baixo do tanque TK-106                 | `INPUT_SENS_SL_TK-106`     |
|                       | `%M13`       | Bomba P-103 em funcionamento                                      | `OUTPUT_RUN_P103`          |
|                       | `%M14`       | Estado RUN do sistema                                             | `MEM_RUN_STATE`            |
|                       | `%M15`       | Alternância de bombas P-102/A e P-102/B                           | `MEM_ALT_P102`             |

## 8. Melhorias Propostas

8.1. **Automação e Monitoramento em Tempo Real**

- Com sensores IoT e análises em tempo real, é possível ajustar automaticamente as dosagens de produtos químicos, minimizando desperdícios e melhorando a qualidade do tratamento. A integração com sistemas permitirá otimizar os parâmetros do processo de tratamento com base no feedback dos sensores, garantindo uma operação mais precisa e reativa. Além disso, a implementação de alarmes visuais e sonoros permitirá uma resposta rápida a eventos críticos, evitando falhas e garantindo a continuidade da operação.

  8.2. **Utilização de Circuitos de Água Fechados**

- Implementar circuitos de água fechados para possibilitar o reaproveitamento máximo da água tratada dentro do processo produtivo. Essa abordagem minimiza o uso de água fresca e reduz o volume de efluentes, ajudando a mitigar o impacto ambiental e os custos associados ao tratamento de água.

  8.3. **Valvulas Pneumáticas e Automação para Dosagem**

- Substituir as válvulas manuais por válvulas pneumáticas para permitir maior precisão na dosagem de polímeros e coagulantes. As válvulas pneumáticas, integradas com o sistema de controle, garantirão uma resposta rápida e precisa aos comandos automáticos, melhorando o controle de dosagem e assegurando a aplicação dos produtos químicos na quantidade exata necessária.

  8.4. **Fechamento de Ciclos e Recuperação de Fibra**

- Implementar tecnologias de filtração avançada e sistemas de separação para o fechamento dos ciclos de processo e a recuperação de fibras. Isso permitirá que as fibras de papel sejam recuperadas eficientemente, reduzindo a necessidade de novas matérias-primas e aumentando a sustentabilidade do processo.

## 9. Referências

- [Pulp and Paper Technology - Latest Innovations Driving Water Treatment in Paper Mills](https://www.pulpandpaper-technology.com/articles/latest-innovations-driving-water-treatment-in-paper-mills)
