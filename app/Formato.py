from fastapi.responses import HTMLResponse

def TablaFormato(tabla, titulo: str) -> HTMLResponse:
   
    tabla_html = tabla.to_html(
        index=False,
        classes='table table-bordered table-striped-columns table-hover text-center',
    )
    html_total = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>{titulo}</title>
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
          rel="stylesheet"
        >
        <style>
            .table thead th {{
                text-align: center;
                vertical-align: middle;
                background-color: #04922b;
                color: white; 
            }} 
        </style>    
    </head>
    <body>
        <div class="container my-5">
            <h2 class="text-center mb-4">{titulo}</h2>
            <div class="table-responsive">
                {tabla_html}
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_total)