from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import logging
import uvicorn
from converters.manager import ConverterManager

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PDF to Markdown Converter",
    description="API para converter PDFs em Markdown com arquitetura modular",
    version="2.0.0"
)

# Inicialização do gerenciador de conversores
logger.info("🚀 Inicializando PDF to Markdown Converter API v2.0")
converter_manager = ConverterManager()

@app.get("/")
async def root():
    """Endpoint de saúde da API"""
    status_info = {
        "message": "PDF to Markdown Converter API v2.0",
        "status": "running",
        "version": "2.0.0",
        "architecture": "modular",
        "timestamp": "2024-01-01T00:00:00Z"
    }
    
    # Adiciona informações dos conversores
    converter_status = converter_manager.get_converter_status()
    status_info.update(converter_status)
    
    # Adiciona recomendações
    recommendations = converter_manager.get_recommendations()
    if recommendations:
        status_info["recommendations"] = recommendations
    
    return status_info

@app.post("/convert-pdf")
async def convert_pdf(file: UploadFile = File(...)):
    """
    Converte um arquivo PDF para Markdown
    
    Args:
        file: Arquivo PDF enviado via upload
        
    Returns:
        JSON com o conteúdo em Markdown
    """
    # Validações
    if not file.filename:
        raise HTTPException(status_code=400, detail="Nome do arquivo não fornecido")
    
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Arquivo deve ser um PDF")
    
    try:
        # Lê o conteúdo do arquivo
        content = await file.read()
        if not content:
            raise HTTPException(status_code=400, detail="Arquivo vazio")
        
        logger.info(f"Arquivo recebido: {file.filename} ({len(content)} bytes)")
        
        # Converte usando o gerenciador de conversores
        result = converter_manager.convert_pdf(content, file.filename)
        
        logger.info(f"Conversão concluída para: {file.filename}")
        return result
                
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")

@app.get("/health")
async def health_check():
    """Endpoint para verificação de saúde da aplicação"""
    converter_status = converter_manager.get_converter_status()
    
    health_info = {
        "status": "healthy",
        "version": "2.0.0",
        "architecture": "modular",
        "timestamp": "2024-01-01T00:00:00Z"
    }
    
    health_info.update(converter_status)
    
    return health_info

@app.get("/converters")
async def list_converters():
    """Lista todos os conversores disponíveis e seus status"""
    return converter_manager.get_converter_status()

@app.get("/converters/{converter_name}")
async def get_converter_status(converter_name: str):
    """Retorna status detalhado de um conversor específico"""
    for converter in converter_manager.converters:
        if converter_name.lower() in converter.name.lower():
            if hasattr(converter, 'get_detailed_status'):
                return converter.get_detailed_status()
            else:
                return converter.get_status()
    
    raise HTTPException(status_code=404, detail=f"Conversor '{converter_name}' não encontrado")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
