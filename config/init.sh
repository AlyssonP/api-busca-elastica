#!/bin/bash
set -e

core_name="cbo"

# Espera o Solr iniciar
echo "Aguardando o Solr iniciar..."
solr start
sleep 5

# Verifica se o core já existe no Solr
if curl -s "http://localhost:8983/solr/admin/cores?action=STATUS" | grep -q "\"${core_name}\""; then
    echo "O core '${core_name}' já existe. Pulando criação."
else
    echo "Criando core '${core_name}'..."
    solr create -c "${core_name}"
    echo "Core '${core_name}' criado com sucesso!"
fi
tail -f /opt/bitnami/solr/logs/solr.log