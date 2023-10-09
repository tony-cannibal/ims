import mariadb


headings = [
    "Centro", "Lugar de montaje", "Denominación", "Lugar de Elaboración",
    "Denominación", "Modelo", "Grupo artíc. externo", "Material",
    "Lista mat.alternat.", "Unidad medida base", "Progreso de Elaboración",
    "Finalización de la elaboración", "Sub en espera", "Finalización de SUB",
    "Finalización de Montaje", "Espera de entrada de mercancías",
    "Stock TRN", "Stock MTY", "Lote", "Estado", "Clase de orden", "QTY",
    "Denom.gr-artículos", "Denom.gpo.artíc.ext.", "Ranking",
    "Descrip.breve"
]

if __name__ == "__main__":
    print(len(headings))
