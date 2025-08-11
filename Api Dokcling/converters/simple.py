"""
Conversor simples que simula a conversão de PDF para Markdown
"""

from .base import BaseConverter
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class SimpleConverter(BaseConverter):
    """Conversor simples que simula a conversão"""
    
    def __init__(self):
        super().__init__(
            name="Simple Converter",
            description="Conversor de simulação para testes e desenvolvimento"
        )
        self.available = True  # Sempre disponível
        logger.info("✅ SimpleConverter inicializado")
    
    def is_available(self) -> bool:
        """Sempre retorna True - este conversor sempre funciona"""
        return True
    
    def convert(self, file_content: bytes, filename: str) -> Dict[str, Any]:
        """Simula a conversão de PDF para Markdown"""
        logger.info(f"Simulando conversão para: {filename}")
        
        # Gera markdown simulado baseado no arquivo
        markdown_content = self._generate_mock_markdown(file_content, filename)
        
        return {
            "success": True,
            "filename": filename,
            "markdown": markdown_content,
            "message": "PDF convertido com sucesso (simulação)",
            "mode": "simple",
            "converter": self.name,
            "note": "Esta é uma versão de simulação para testes"
        }
    
    def _generate_mock_markdown(self, file_content: bytes, filename: str) -> str:
        """Gera markdown simulado baseado no arquivo"""
        file_size = len(file_content)
        
        # Simula diferentes tipos de conteúdo baseado no tamanho
        if file_size < 1000:
            content_type = "documento pequeno"
        elif file_size < 10000:
            content_type = "documento médio"
        else:
            content_type = "documento grande"
        
        return f"""# Documento convertido: {filename}

Este é um exemplo de markdown convertido do PDF usando o conversor simples.

## Informações do arquivo:
- **Nome original**: {filename}
- **Tamanho**: {file_size} bytes
- **Tipo**: PDF
- **Classificação**: {content_type}

## Conteúdo simulado:
Este é um conteúdo de exemplo que simula a conversão real do PDF para Markdown.

### Seções simuladas:
1. **Introdução**: Texto de exemplo para {filename}
2. **Desenvolvimento**: Conteúdo simulado baseado no tamanho do arquivo
3. **Conclusão**: Final do documento simulado

### Detalhes técnicos:
- **Conversor usado**: {self.name}
- **Modo**: Simulação
- **Timestamp**: 2024-01-01T00:00:00Z

---
*Nota: Esta é uma versão de simulação. Para conversão real, use um conversor como Docling.*
"""
