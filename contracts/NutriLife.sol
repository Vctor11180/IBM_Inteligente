// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract NutriLife {
    // ============ STRUCTS ============
    
    struct AnalisisNutricional {
        address usuario;
        string cidIPFS;
        bool porcionCorrecta;
        uint256 confianza;    // 0-100
        uint256 calorias;
        uint256 timestamp;
        uint256 idAnalisis;
    }
    
    struct EstadisticasUsuario {
        uint256 totalAnalisis;
        uint256 porcionesCorrectas;
        uint256 excesos;
        uint256 caloriasTotales;
        uint256 caloriasPromedio;
        uint256 confianzaPromedio;
    }
    
    // ============ STATE VARIABLES ============
    
    mapping(address => uint256[]) public analisisPorUsuario;
    mapping(uint256 => AnalisisNutricional) public analisisPorId;
    
    // Estadísticas por usuario (actualizadas automáticamente)
    mapping(address => EstadisticasUsuario) public estadisticasUsuario;
    
    uint256 private contadorAnalisis;
    address public owner;
    
    // ============ EVENTS ============
    
    event AnalisisGuardado(
        address indexed usuario,
        uint256 indexed idAnalisis,
        string cidIPFS,
        bool porcionCorrecta,
        uint256 confianza,
        uint256 calorias,
        uint256 timestamp
    );
    
    // ============ MODIFIERS ============
    
    modifier soloOwner() {
        require(msg.sender == owner, "Solo el owner puede ejecutar");
        _;
    }
    
    // ============ CONSTRUCTOR ============
    
    constructor() {
        owner = msg.sender;
        contadorAnalisis = 0;
    }
    
    // ============ FUNCTIONS ============
    
    /**
     * @dev Guarda un nuevo análisis nutricional y actualiza estadísticas
     * @param cidIPFS CID de la imagen en IPFS
     * @param porcionCorrecta true si es porción correcta, false si es exceso
     * @param confianza Nivel de confianza del modelo (0-100)
     * @param calorias Calorías estimadas
     * @return ID del análisis guardado
     */
    function guardarAnalisis(
        string memory cidIPFS,
        bool porcionCorrecta,
        uint256 confianza,
        uint256 calorias
    ) public returns (uint256) {
        // Validaciones
        require(bytes(cidIPFS).length > 0, "CID IPFS no puede estar vacio");
        require(confianza <= 100, "Confianza debe ser entre 0 y 100");
        require(calorias > 0, "Calorias deben ser mayores a 0");
        
        // Incrementar contador
        contadorAnalisis++;
        
        // Crear nuevo análisis
        AnalisisNutricional memory nuevoAnalisis = AnalisisNutricional({
            usuario: msg.sender,
            cidIPFS: cidIPFS,
            porcionCorrecta: porcionCorrecta,
            confianza: confianza,
            calorias: calorias,
            timestamp: block.timestamp,
            idAnalisis: contadorAnalisis
        });
        
        // Guardar en storage
        analisisPorId[contadorAnalisis] = nuevoAnalisis;
        analisisPorUsuario[msg.sender].push(contadorAnalisis);
        
        // Actualizar estadísticas del usuario
        actualizarEstadisticas(msg.sender, porcionCorrecta, confianza, calorias);
        
        // Emitir evento
        emit AnalisisGuardado(
            msg.sender,
            contadorAnalisis,
            cidIPFS,
            porcionCorrecta,
            confianza,
            calorias,
            block.timestamp
        );
        
        return contadorAnalisis;
    }
    
    /**
     * @dev Actualiza las estadísticas de un usuario después de guardar un análisis
     * @param usuario Dirección del usuario
     * @param porcionCorrecta Si la porción fue correcta o no
     * @param confianza Confianza del análisis (0-100)
     * @param calorias Calorías del análisis
     */
    function actualizarEstadisticas(
        address usuario,
        bool porcionCorrecta,
        uint256 confianza,
        uint256 calorias
    ) private {
        EstadisticasUsuario storage stats = estadisticasUsuario[usuario];
        
        // Incrementar contadores
        stats.totalAnalisis++;
        
        if (porcionCorrecta) {
            stats.porcionesCorrectas++;
        } else {
            stats.excesos++;
        }
        
        // Actualizar calorías
        stats.caloriasTotales += calorias;
        stats.caloriasPromedio = stats.caloriasTotales / stats.totalAnalisis;
        
        // Actualizar confianza promedio
        // Si es el primer análisis, usar directamente la confianza
        // Si no, calcular promedio: (confianza_promedio_anterior * (n-1) + confianza_nueva) / n
        if (stats.totalAnalisis == 1) {
            stats.confianzaPromedio = confianza;
        } else {
            uint256 nuevaConfianzaPromedio = (stats.confianzaPromedio * (stats.totalAnalisis - 1) + confianza) / stats.totalAnalisis;
            stats.confianzaPromedio = nuevaConfianzaPromedio;
        }
    }
    
    /**
     * @dev Obtiene un análisis específico por ID
     */
    function obtenerAnalisis(uint256 idAnalisis) 
        public 
        view 
        returns (
            address usuario,
            string memory cidIPFS,
            bool porcionCorrecta,
            uint256 confianza,
            uint256 calorias,
            uint256 timestamp
        ) 
    {
        AnalisisNutricional memory analisis = analisisPorId[idAnalisis];
        require(analisis.idAnalisis != 0, "Analisis no existe");
        
        return (
            analisis.usuario,
            analisis.cidIPFS,
            analisis.porcionCorrecta,
            analisis.confianza,
            analisis.calorias,
            analisis.timestamp
        );
    }
    
    /**
     * @dev Obtiene todos los IDs de análisis de un usuario
     */
    function obtenerAnalisisUsuario(address usuario) 
        public 
        view 
        returns (uint256[] memory) 
    {
        return analisisPorUsuario[usuario];
    }
    
    /**
     * @dev Obtiene las estadísticas de un usuario
     */
    function obtenerEstadisticasUsuario(address usuario) 
        public 
        view 
        returns (
            uint256 totalAnalisis,
            uint256 porcionesCorrectas,
            uint256 excesos,
            uint256 caloriasTotales,
            uint256 caloriasPromedio,
            uint256 confianzaPromedio
        ) 
    {
        EstadisticasUsuario memory stats = estadisticasUsuario[usuario];
        
        return (
            stats.totalAnalisis,
            stats.porcionesCorrectas,
            stats.excesos,
            stats.caloriasTotales,
            stats.caloriasPromedio,
            stats.confianzaPromedio
        );
    }
    
    /**
     * @dev Cuenta cuántos análisis tiene un usuario
     */
    function contarAnalisisUsuario(address usuario) 
        public 
        view 
        returns (uint256) 
    {
        return analisisPorUsuario[usuario].length;
    }
    
    /**
     * @dev Obtiene el total de análisis guardados (estadística global)
     */
    function obtenerTotalAnalisis() public view returns (uint256) {
        return contadorAnalisis;
    }
}

