form flask import Blueprint

band_bp =Blueprint('band_bp',__name__)

@band_bp('/bands', methods=['GET'])
    print("Hola Moni")

@band_bp('/bands/<int:band_id>', methods=['GET'])
    print("Hola Moni")
@band_bp('/bands', methods=['POST'])
    print("Hola Moni")
@band_bp('/bands/<int:band_id>', methods=['PUT'])
    print("Hola Moni")
@band_bp('/bands/<int:band_id>', methods=['DELETE'])