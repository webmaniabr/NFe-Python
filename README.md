<p align="center">
  <img src="https://wmbr.s3.amazonaws.com/img/logo_webmaniabr_github2.png">
</p>

# NFe-Python

Através do emissor de Nota Fiscal da Webmania®, você conta com a emissão e arquivamento das suas notas fiscais, cálculo automático de impostos, geração do Danfe para impressão e envio automático de e-mails para os clientes. Realize a integração com o seu sistema utilizando a nossa REST API.

- Emissor de Nota Fiscal Webmania®: [Saiba mais](https://webmaniabr.com/nota-fiscal-eletronica/)
- Documentação da REST API: [Visualizar](https://webmaniabr.com/docs/rest-api-nfe/)

## Requisitos

- Contrate um dos planos de Nota Fiscal Eletrônica da Webmania® (Teste 30 dias grátis): [Assine agora mesmo](https://webmaniabr.com/nota-fiscal-eletronica/).
- Possuir a versão do Python 2.0 ou inferior.
- Instalar a biblioteca [Requests](http://docs.python-requests.org/en/master/).
- Realize a integração com o seu sistema.

## Exemplos

Desenvolvimento baseado na biblioteca [Requests](http://docs.python-requests.org/en/master/).

- **cancelarNotaFiscal**: Cancelar Nota Fiscal enviada ao SEFAZ.
- **cartaCorrecao**: Corrigir uma Nota Fiscal junto ao SEFAZ.
- **consultarNotaFiscal**: Consulta a Nota Fiscal enviada para o SEFAZ.
- **emitirNotaFiscal_Armamentos**: Emissão da Nota Fiscal com detalhamento específico de Armamentos.
- **emitirNotaFiscal_Combustivel**: Emissão da Nota Fiscal com detalhamento específico de Combustivel.
- **emitirNotaFiscal_Medicamentos**: Emissão da Nota Fiscal com detalhamento específico de Medicamentos.
- **emitirNotaFiscal_Rastreabilidade**: Emissão da Nota Fiscal com detalhamento específico de Rastreabilidade.
- **emitirNotaFiscal_VeiculosNovos**: Emissão da Nota Fiscal com detalhamento específico de Veiculos Novos.
- **emitirNotaFiscal**: Emissão da Nota Fiscal junto ao SEFAZ.
- **emitirNotaFiscalAjuste**: Emite uma nota fiscal de ajuste.
- **emitirNotaFiscalComplementar_Imposto**: Emite uma Nota Fiscal complementar.
- **emitirNotaFiscalComplementar_PrecoQuantidade**: Emite uma Nota Fiscal complementar.
- **emitirNotaFiscalDevolucao**: Emissão de Nota Fiscal de devolução junto ao SEFAZ.
- **inutilizarNumeracao**: Inutilizar sequência de numeração junto ao SEFAZ.
- **statusSefaz**: Verifica se o Sefaz está Online ou Offline.
- **validadeCertificadoA1**: Verifica se o Certificado A1 é válido e quantos dias faltam para expirar.

## Suporte

Qualquer dúvida entre em contato na nossa [Central de Ajuda](https://ajuda.webmaniabr.com) ou acesse o [Painel de Controle](https://webmaniabr.com/painel/) para conversar em tempo real no Chat ou Abrir um chamado.
