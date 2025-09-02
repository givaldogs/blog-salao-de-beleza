#!/bin/bash

SERVICE_NAME="blog.service"  # Altere para o nome do seu serviço, se precisar

case "$1" in
  restart)
    echo "Reiniciando serviço $SERVICE_NAME..."
    sudo systemctl restart $SERVICE_NAME
    ;;

  status)
    echo "Mostrando status do serviço $SERVICE_NAME..."
    sudo systemctl status $SERVICE_NAME
    ;;

  kill)
    echo "Encerrando todos os processos gunicorn..."
    pkill gunicorn
    ;;

  start)
    echo "Iniciando Gunicorn manualmente..."
    gunicorn project.wsgi:application --bind 0.0.0.0:8000 --daemon
    ;;

  *)
    echo "Uso: $0 {restart|status|kill|start}"
    ;;
esac
