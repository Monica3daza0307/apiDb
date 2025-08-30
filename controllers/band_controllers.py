form flask import Blueprint

band_bp =Blueprint('band_bp',__name__)

@band_bp('/bands', methods=['GET'])

@band_bp('/bands/<int:band_id>', methods=['GET'])

@band_bp('/bands', methods=['POST'])

@band_bp('/bands/<int:band_id>', methods=['PUT'])

@band_bp('/bands/<int:band_id>', methods=['DELETE'])