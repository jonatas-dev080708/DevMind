#!/usr/bin/env python3
"""
Script de teste para a API PDF to Markdown Converter v2.0
Demonstra como usar corretamente todos os endpoints
"""

import requests
import json
import os
from pathlib import Path

# Configuração da API
API_BASE_URL = "http://localhost:8000"

def test_api_endpoints():
    """Testa todos os endpoints da API"""
    
    print("🚀 Testando API PDF to Markdown Converter v2.0")
    print("=" * 60)
    
    # 1. Teste do endpoint raiz
    print("\n1️⃣ Testando endpoint raiz (/)")
    try:
        response = requests.get(f"{API_BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {data.get('status')}")
            print(f"✅ Versão: {data.get('version')}")
            print(f"✅ Arquitetura: {data.get('architecture')}")
        else:
            print(f"❌ Erro: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
    
    # 2. Teste do health check
    print("\n2️⃣ Testando health check (/health)")
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status: {data.get('status')}")
        else:
            print(f"❌ Erro: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
    
    # 3. Teste da lista de conversores
    print("\n3️⃣ Testando lista de conversores (/converters)")
    try:
        response = requests.get(f"{API_BASE_URL}/converters")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Conversores disponíveis: {len(data.get('converters', []))}")
            for converter in data.get('converters', []):
                print(f"   - {converter.get('name')}: {converter.get('status')}")
        else:
            print(f"❌ Erro: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
    
    # 4. Teste do endpoint de conversão (sem arquivo)
    print("\n4️⃣ Testando endpoint de conversão (/convert-pdf) - SEM arquivo")
    try:
        response = requests.post(f"{API_BASE_URL}/convert-pdf")
        if response.status_code == 422:  # Erro esperado - arquivo não fornecido
            print("✅ Endpoint funcionando - erro esperado (arquivo não fornecido)")
        else:
            print(f"⚠️ Status inesperado: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")

def test_with_sample_pdf():
    """Testa a conversão com um PDF de exemplo (se disponível)"""
    
    print("\n5️⃣ Testando conversão com PDF de exemplo")
    
    # Procura por arquivos PDF no diretório atual
    pdf_files = list(Path(".").glob("*.pdf"))
    
    if not pdf_files:
        print("⚠️ Nenhum arquivo PDF encontrado para teste")
        print("💡 Para testar a conversão, coloque um arquivo PDF no diretório do projeto")
        return
    
    # Usa o primeiro PDF encontrado
    pdf_file = pdf_files[0]
    print(f"📄 Usando arquivo: {pdf_file.name}")
    
    try:
        with open(pdf_file, "rb") as f:
            files = {"file": (pdf_file.name, f, "application/pdf")}
            response = requests.post(f"{API_BASE_URL}/convert-pdf", files=files)
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Conversão realizada com sucesso!")
                print(f"📝 Tamanho do markdown: {len(data.get('markdown', ''))} caracteres")
                print(f"🔧 Conversor usado: {data.get('converter_used', 'N/A')}")
            else:
                print(f"❌ Erro na conversão: {response.status_code}")
                print(f"📄 Detalhes: {response.text}")
                
    except Exception as e:
        print(f"❌ Erro ao processar arquivo: {e}")

def show_usage_examples():
    """Mostra exemplos de uso da API"""
    
    print("\n📚 Exemplos de Uso da API:")
    print("=" * 60)
    
    print("\n🌐 Acesse a documentação interativa:")
    print(f"   {API_BASE_URL}/docs")
    
    print("\n📡 Endpoints disponíveis:")
    print(f"   GET  {API_BASE_URL}/")
    print(f"   POST {API_BASE_URL}/convert-pdf")
    print(f"   GET  {API_BASE_URL}/health")
    print(f"   GET  {API_BASE_URL}/converters")
    
    print("\n🔧 Teste com cURL:")
    print(f"   # Status da API")
    print(f"   curl {API_BASE_URL}/")
    print(f"   ")
    print(f"   # Converter PDF")
    print(f"   curl -X POST -F 'file=@seu_arquivo.pdf' {API_BASE_URL}/convert-pdf")
    
    print("\n🐍 Teste com Python requests:")
    print("   import requests")
    print("   files = {'file': open('arquivo.pdf', 'rb')}")
    print(f"   response = requests.post('{API_BASE_URL}/convert-pdf', files=files)")
    print("   print(response.json())")

def main():
    """Função principal"""
    
    # Verifica se a API está rodando
    try:
        response = requests.get(f"{API_BASE_URL}/", timeout=5)
        if response.status_code != 200:
            print("❌ API não está respondendo corretamente")
            print("💡 Certifique-se de que a API está rodando com: python start.py")
            return
    except:
        print("❌ Não foi possível conectar com a API")
        print("💡 Certifique-se de que a API está rodando com: python start.py")
        return
    
    # Executa os testes
    test_api_endpoints()
    test_with_sample_pdf()
    show_usage_examples()
    
    print("\n🎯 Teste concluído!")
    print("💡 Use a documentação interativa para mais detalhes: http://localhost:8000/docs")

if __name__ == "__main__":
    main()
