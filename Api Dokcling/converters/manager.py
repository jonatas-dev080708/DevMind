#!/usr/bin/env python3
"""
Gerenciador de conversores simplificado
Foca apenas no essencial para conversão PDF -> Markdown
"""

import logging
from typing import Dict, Any, List
from .simple_pdf import SimplePDFConverter

logger = logging.getLogger(__name__)

class ConverterManager:
    """Gerenciador simplificado de conversores PDF"""
    
    def __init__(self):
        """Inicializa o gerenciador com conversores essenciais"""
        logger.info("🔧 Inicializando conversores essenciais...")
        
        # Lista de conversores disponíveis
        self.converters: List[Any] = []
        
        # Inicializa conversores
        self._initialize_converters()
        
        # Seleciona o conversor ativo
        self.active_converter = self._select_active_converter()
        
        logger.info(f"✅ {len(self.converters)} conversores inicializados")
        if self.active_converter:
            logger.info(f"🎯 Conversor ativo: {self.active_converter.name}")
    
    def _initialize_converters(self):
        """Inicializa os conversores disponíveis"""
        try:
            # Conversor principal (PDF real)
            pdf_converter = SimplePDFConverter()
            self.converters.append(pdf_converter)
            
        except Exception as e:
            logger.error(f"❌ Erro ao inicializar conversores: {e}")
    
    def _select_active_converter(self):
        """Seleciona o conversor ativo baseado na disponibilidade"""
        # Prioriza conversores reais sobre fallbacks
        for converter in self.converters:
            if hasattr(converter, 'available') and converter.available:
                return converter
        
        # Se não houver conversores reais, usa o primeiro disponível
        if self.converters:
            return self.converters[0]
        
        return None
    
    def convert_pdf(self, pdf_content: bytes, filename: str) -> Dict[str, Any]:
        """
        Converte PDF para Markdown usando o conversor ativo
        
        Args:
            pdf_content: Conteúdo do arquivo PDF em bytes
            filename: Nome do arquivo PDF
            
        Returns:
            Dicionário com o resultado da conversão
        """
        if not self.active_converter:
            return self._error_response(filename, "Nenhum conversor disponível")
        
        try:
            logger.info(f"🔄 Convertendo {filename} usando {self.active_converter.name}")
            return self.active_converter.convert_pdf(pdf_content, filename)
            
        except Exception as e:
            logger.error(f"❌ Erro na conversão: {e}")
            return self._error_response(filename, str(e))
    
    def _error_response(self, filename: str, error_message: str) -> Dict[str, Any]:
        """Gera resposta de erro padronizada"""
        return {
            "success": False,
            "filename": filename,
            "error": error_message,
            "converter_used": "None",
            "mode": "error"
        }
    
    def get_converter_status(self) -> Dict[str, Any]:
        """Retorna status dos conversores"""
        if not self.converters:
            return {
                "total_converters": 0,
                "available_converters": 0,
                "converters": [],
                "active_converter": None,
                "conversion_capability": "none"
            }
        
        available_count = sum(1 for c in self.converters if hasattr(c, 'available') and c.available)
        
        converter_status = []
        for converter in self.converters:
            if hasattr(converter, 'get_status'):
                converter_status.append(converter.get_status())
            else:
                converter_status.append({
                    "name": getattr(converter, 'name', 'Unknown'),
                    "status": "unknown"
                })
        
        # Determina capacidade de conversão
        if available_count > 0:
            capability = "real"
        elif self.converters:
            capability = "fallback"
        else:
            capability = "none"
        
        return {
            "total_converters": len(self.converters),
            "available_converters": available_count,
            "converters": converter_status,
            "active_converter": self.active_converter.get_status() if self.active_converter else None,
            "conversion_capability": capability,
            "mode": "essential"  # Modo essencial
        }
    
    def get_recommendations(self) -> List[str]:
        """Retorna recomendações para melhorar a conversão"""
        recommendations = []
        
        if not self.converters:
            recommendations.append("Instale as dependências básicas: pip install pypdf2 pdfplumber")
            return recommendations
        
        # Verifica se há conversores reais
        has_real_converter = any(
            hasattr(c, 'available') and c.available 
            for c in self.converters
        )
        
        if not has_real_converter:
            recommendations.append("Para conversão completa, instale: pip install pypdf2 pdfplumber")
            recommendations.append("Estas bibliotecas permitem extração real de texto de PDFs")
        
        return recommendations
