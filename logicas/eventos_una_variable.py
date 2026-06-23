def configurar_unidad(
    panel,
    destino,
    origenes
):
    panel.destino = destino

    panel.label_destino.SetLabel(
        f"Destino: {destino}"
    )

    panel.combo_origen.Clear()

    panel.combo_origen.AppendItems(
        origenes
    )

    panel.combo_origen.SetSelection(0)

    panel.origen = panel.combo_origen.GetValue()

# ===================
# EVENTOS LONGITUD  =
# ===================

def opcion_cm(panel):
    configurar_unidad(
        panel,
        "Centimetros",
        [
            "Pulgadas",
            "Pies",
            "Yardas"
        ]
    )


def opcion_pies(panel):
    configurar_unidad(
        panel,
        "Pies",
        [
            "Centimetros",
            "Pulgadas",
            "Yardas"
        ]
    )


def opcion_pulgadas(panel):
    configurar_unidad(
        panel,
        "Pulgadas",
        [
            "Centimetros",
            "Pies",
            "Yardas"
        ]
    )


def opcion_yardas(panel):
    configurar_unidad(
        panel,
        "Yardas",
        [
            "Centimetros",
            "Pies",
            "Pulgadas"
        ]
    )

    # ===============    
    #  EVENTOS PESO =
    # ===============

def opcion_gramos(panel):
    configurar_unidad(
        panel,
        "Gramos",
        [
            "Kilogramos",
            "Libras",
            "Toneladas",
            "Onzas"
        ]
    )


def opcion_kilogramos(panel):
    configurar_unidad(
        panel,
        "Kilogramos",
        [
            "Gramos",
            "Libras",
            "Toneladas",
            "Onzas"
        ]
    )


def opcion_libras(panel):
    configurar_unidad(
        panel,
        "Libras",
        [
            "Gramos",
            "Kilogramos",
            "Toneladas",
            "Onzas"
        ]
    )


def opcion_toneladas(panel):
    configurar_unidad(
        panel,
        "Toneladas",
        [
            "Gramos",
            "Kilogramos",
            "Libras",
            "Onzas"
        ]
    )


def opcion_onzas(panel):
    configurar_unidad(
        panel,
        "Onzas",
        [
            "Gramos",
            "Kilogramos",
            "Libras",
            "Toneladas"
        ]
    )

    # =====================
    # EVENTOS TEMPERATURA =
    # =====================

def opcion_celsius(panel):
    configurar_unidad(
        panel,
        "Celsius",
        [
            "Fahrenheit",
            "Kelvin"
        ]
    )

def opcion_fahrenheit(panel):
    configurar_unidad(
        panel,
        "Fahrenheit",
    [
            "Celsius",
            "Kelvin"
    ]
    )

def opcion_kelvin(panel):
    configurar_unidad(
        panel,
        "Kelvin",
    [
            "Celsius",
            "Fahrenheit"
    ]
    )
            

# ===========================
# EVENTOS DATOS INFORMATICOS=
# ===========================

def opcion_bits(panel):
    configurar_unidad(
        panel,
        "Bits",
        [
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes"
        ]
    )

def opcion_bytes(panel):
    configurar_unidad(
        panel,
        "Bytes",
        [
            "Bits",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes"
        ]
    )

def opcion_kilobytes(panel):
    configurar_unidad(
        panel,
        "Kilobytes",
        [
            "Bits",
            "Bytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes"
        ]
    )

def opcion_megabytes(panel):
    configurar_unidad(
        panel,
        "Megabytes",
        [
            "Bits",
            "Bytes",
            "Kilobytes",
            "Gigabytes",
            "Terabytes"
        ]
    )

def opcion_gigabytes(panel):
    configurar_unidad(
        panel,
        "Gigabytes",
        [
            "Bits",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Terabytes"
        ]
    )

def opcion_terabytes(panel):
    configurar_unidad(
        panel,
        "Terabytes",
        [
            "Bits",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes"
            
        ]
    )
