#Inicio
pip install selenium
 >Estrutura

    {{Nome do Projeto}}
        python
            poms
                {{funcionalidade}}
                    {{SubFuncionalidade.py}} -classes com locators e metodos exclusivos 
            testes
                {{funcionalidade}}
                    {{SubFuncionalidadeTest.py}} - Classe com os casos de teste implementados
                testConfig.py - Classe que executa funções antes e depois da execução do test, ex: cria webdriver, conecta com jira etc.
            utils
                CreateStep.py - Gerar Objeto Step
                JiraConnection.py - Metodos para conectar ao Jira via API
                Login.py - Login ao sistema
                TestReport.py - Criar Report dos testes em arquivo
                Tools.py - Tira print, grava video e etc.
        resources
            files
                input - caso exista, inserir arquivo de entrada de dados nos testes (deve ser manipulado)
                output - saida de arquivos de execucao, imagens e videos dos testes e etc.
            webdrives - drives para consumo do  selenium
                cromedriver
                gechodriver
                internetExplorerdriver
        test_report
            Relatorio de testes, alinhar se sera html, PDF, xml, excel etc. 
