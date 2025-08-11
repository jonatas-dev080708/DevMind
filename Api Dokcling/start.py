#!/usr/bin/env python3
"""
Script de inicialização para a API PDF to Markdown Converter v2.0
"""

import os
import sys
import uvicorn
from dotenv import load_dotenv

def load_environment():
    """Carrega variáveis de ambiente do arquivo .env"""
    env_file = ".env"
    if os.path.exists(env_file):
        load_dotenv(env_file)
        print(f"✅ Variáveis de ambiente carregadas de {env_file}")
    else:
        print("⚠️  Arquivo .env não encontrado, usando configurações padrão")

def get_config():
    """Obtém configurações do servidor"""
    return {
        "host": os.getenv("HOST", "0.0.0.0"),
        "port": int(os.getenv("PORT", "8000")),
        "log_level": os.getenv("LOG_LEVEL", "info"),
        "reload": os.getenv("ENVIRONMENT", "development") == "development",
        "architecture": "modular"  # Nova arquitetura sempre ativa
    }

def main():
    """Função principal"""
    print("🚀 Iniciando PDF to Markdown Converter API v2.0")
    print("=" * 60)
    print("🏗️  Nova arquitetura modular com fallback automático")
    print("=" * 60)
    
    # Carrega variáveis de ambiente
    load_environment()
    
    # Obtém configurações
    config = get_config()
    
    # Nova arquitetura sempre usa main.py
    app_file = "main:app"
    architecture_description = "Arquitetura Modular v2.0"
    
    print(f"📋 Configurações:")
    print(f"   Host: {config['host']}")
    print(f"   Porta: {config['port']}")
    print(f"   Log Level: {config['log_level']}")
    print(f"   Reload: {config['reload']}")
    print(f"   Ambiente: {os.getenv('ENVIRONMENT', 'development')}")
    print(f"   Arquitetura: {architecture_description}")
    
    print("\n🔧 Inicializando conversores...")
    print("📖 Documentação disponível em: http://{config['host']}:{config['port']}/docs")
    print(f"🏥 Health check: http://{config['host']}:{config['port']}/health")
    print(f"🔍 Status dos conversores: http://{config['host']}:{config['port']}/converters")
    
    try:
        uvicorn.run(
            app_file,
            host=config["host"],
            port=config["port"],
            reload=config["reload"],
            log_level=config["log_level"]
        )
    except KeyboardInterrupt:
        print("\n\n👋 Servidor interrompido pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao iniciar servidor: {e}")
        print("\n💡 Verifique se todos os arquivos estão presentes:")
        print("   - converters/__init__.py")
        print("   - converters/base.py")
        print("   - converters/simple.py")
        print("   - converters/docling.py")
        print("   - converters/manager.py")
        print("   - main.py")
        sys.exit(1)

if __name__ == "__main__":
    main()
