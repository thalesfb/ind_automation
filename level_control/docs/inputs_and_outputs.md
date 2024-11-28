# Mapeamento de Entradas, Saídas e Memórias

| **Tipo**              | **Endereço** | **Descrição**                                           | **Símbolo**              |
| --------------------- | ------------ | ------------------------------------------------------- | ------------------------ |
| **Entradas Digitais** | `%I0.0`      | Sensor de nível muito alto no tanque TK-101             | `INPUT_LTHH_TK101`       |
|                       | `%I0.1`      | Sensor de nível alto no tanque TK-101                   | `INPUT_LTH_TK101`        |
|                       | `%I0.2`      | Sensor de nível muito baixo no tanque TK-101            | `INPUT_LTLL_TK101`       |
|                       | `%I0.2`      | Sensor de nível muito alto no tanque TK-103/A           | `INPUT_LTHH_TK103_A`     |
|                       | `%I0.3`      | Sensor de nível muito baixo no tanque TK-103/A          | `INPUT_LTLL_TK103_A`     |
|                       | `%I0.4`      | Sensor de nível muito alto no tanque TK-103/B           | `INPUT_LTHH_TK103_B`     |
|                       | `%I0.5`      | Sensor de nível muito baixo no tanque TK-103/B          | `INPUT_LTLL_TK103_B`     |
|                       | `%I0.6`      | Sensor de nível muito alto no tanque TK-104/A           | `INPUT_LTHH_TK104_A`     |
|                       | `%I0.7`      | Sensor de nível muito baixo no tanque TK-104/A          | `INPUT_LTLL_TK104_A`     |
|                       | `%I1.0`      | Sensor de nível muito alto no tanque TK-104/B           | `INPUT_LTHH_TK104_B`     |
|                       | `%I1.1`      | Sensor de nível muito baixo no tanque TK-104/B          | `INPUT_LTLL_TK104_B`     |
|                       | `%I1.2`      | Botão Start do sistema                                  | `INPUT_START_BUTTON`     |
|                       | `%I1.3`      | Botão Stop do sistema                                   | `INPUT_STOP_BUTTON`      |
|                       | `%I1.4`      | Falha na bomba P-101A                                   | `INPUT_FAULT_P101A`      |
|                       | `%I1.5`      | Falha na bomba P-101B                                   | `INPUT_FAULT_P101B`      |
| **Saídas Digitais**   | `%Q0.0`      | Acionamento da bomba P-101 para abastecimento do TK-102 | `OUTPUT_RUN_P101`        |
|                       | `%Q0.2`      | Acionamento da bomba P-102/A                            | `OUTPUT_RUN_P102A`       |
|                       | `%Q0.3`      | Acionamento da bomba P-102/B                            | `OUTPUT_RUN_P102B`       |
|                       | `%Q0.4`      | Acionamento da bomba P-103 de água fresca               | `OUTPUT_RUN_P103`        |
|                       | `%Q0.5`      | Acionamento da bomba P-104 da dosagem do coagulante     | `OUTPUT_RUN_P104`        |
|                       | `%Q0.6`      | Acionamento da bomba P-105 da dosagem do polímero       | `OUTPUT_RUN_P105`        |
|                       | `%Q0.7`      | Acionamento do flotador                                 | `OUTPUT_RUN_FLOAT`       |
|                       | `%Q0.8`      | Alarme sonoro                                           | `OUTPUT_ALARM`           |
|                       | `%Q0.9`      | Agitador do TK-103/A                                    | `OUTPUT_RUN_AGT_TK103_A` |
|                       | `%Q0.10`     | Agitador do TK-103/B                                    | `OUTPUT_RUN_AGT_TK103_B` |
|                       | `%Q0.11`     | Agitador do TK-104/A                                    | `OUTPUT_RUN_AGT_TK104_A` |
|                       | `%Q0.12`     | Agitador do TK-104/B                                    | `OUTPUT_RUN_AGT_TK104_B` |
|                       | `%Q0.13`     | Abertura da válvula pneumática para entrada de água do TK-103/A | `OUTPUT_OPEN_VLV_TK103_A`|
|                       | `%Q0.14`     | Abertura da válvula pneumática para entrada de água do TK-103/B | `OUTPUT_OPEN_VLV_TK103_B`|
|                       | `%Q0.15`     | Abertura da válvula pneumática para entrada de água do TK-104/A | `OUTPUT_OPEN_VLV_TK104_A`|
|                       | `%Q1.0`      | Abertura da válvula pneumática para entrada de água do TK-104/B | `OUTPUT_OPEN_VLV_TK104_B`|
|                       | `%Q1.1`      | Fechamento da válvula pneumática para entrada de água do TK-103/A | `OUTPUT_CLOSE_VLV_TK103_A`|
|                       | `%Q1.2`      | Fechamento da válvula pneumática para entrada de água do TK-103/B | `OUTPUT_CLOSE_VLV_TK103_B`|
|                       | `%Q1.3`      | Fechamento da válvula pneumática para entrada de água do TK-104/A | `OUTPUT_CLOSE_VLV_TK104_A`|
|                       | `%Q1.4`      | Fechamento da válvula pneumática para entrada de água do TK-104/B | `OUTPUT_CLOSE_VLV_TK104_B`|
| **Memórias Internas** | `%M0`        | Sensor de leitura de nível em 80% do TK-101             | `INPUT_SENS_S1_TK-101`   |
|                       | `%M1`        | Sensor de leitura de nível em 50% do TK-101             | `INPUT_SENS_S2_TK-101`   |
|                       | `%M2`        | Sensor de leitura de nível em 20% do TK-101             | `INPUT_SENS_S3_TK-101`   |
|                       | `%M3`        | Sensor de leitura de nível alto do tanque TK-103/A      | `INPUT_SENS_SH_TK-103_A` |
|                       | `%M4`        | Sensor de leitura de nível baixo do tanque TK-103/A     | `INPUT_SENS_SL_TK-103_A` |
|                       | `%M5`        | Sensor de leitura de nível alto do tanque TK-103/B      | `INPUT_SENS_SH_TK-103_B` |
|                       | `%M6`        | Sensor de leitura de nível baixo do tanque TK-103/B     | `INPUT_SENS_SL_TK-103_B` |
|                       | `%M7`        | Sensor de leitura de nível alto do tanque TK-104/A      | `INPUT_SENS_SH_TK-104_A` |
|                       | `%M8`        | Sensor de leitura de nível baixo do tanque TK-104/A     | `INPUT_SENS_SL_TK-104_A` |
|                       | `%M9`        | Sensor de leitura de nível alto do tanque TK-104/B      | `INPUT_SENS_SH_TK-104_B` |
|                       | `%M10`       | Sensor de leitura de nível baixo do tanque TK-104/B     | `INPUT_SENS_SL_TK-104_B` |
|                       | `%M11`       | Sensor de leitura de nível alto do tanque TK-106        | `INPUT_SENS_SH_TK-106`   |
|                       | `%M12`       | Sensor de leitura de nível baixo do tanque TK-106       | `INPUT_SENS_SL_TK-106`   |
|                       | `%M13`       | Bomba P-103 em funcionamento                            | `OUTPUT_RUN_P103`        |
|                       | `%M14`       | Estado RUN do sistema                                   | `MEM_RUN_STATE`          |
|                       | `%M15`       | Alternância de bombas P-102/A e P-102/B                 | `MEM_ALT_P102`           |