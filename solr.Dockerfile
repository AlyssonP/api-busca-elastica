FROM bitnami/solr:latest

# Alternar para root para copiar os arquivos
USER root

COPY config/init.sh /init.sh

# Ajusta as permissões do script
RUN chmod +x /init.sh && chown 1001:1001 /init.sh

# Voltar para o usuário Solr
USER 1001

# Criar o core no Solr na inicialização
CMD ["/init.sh"]
