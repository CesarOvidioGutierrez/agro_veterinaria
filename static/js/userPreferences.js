/**
 * Gestión de preferencias de usuario usando localStorage
 * Depende de localStorage.js
 */

const UserPreferences = {
    // Claves para localStorage
    KEYS: {
        DARK_MODE: 'agro_dark_mode',
        LAST_VIEWED_PRODUCT: 'agro_last_product',
        LAST_VIEWED_CATEGORY: 'agro_last_category',
        ITEMS_PER_PAGE: 'agro_items_per_page'
    },

    /**
     * Establece el modo oscuro
     * @param {boolean} isDarkMode - true para modo oscuro, false para modo claro
     */
    setDarkMode: function(isDarkMode) {
        console.log('setDarkMode llamado con:', isDarkMode);
        AgroLocalStorage.save(this.KEYS.DARK_MODE, isDarkMode);
        this.applyDarkMode();
    },

    /**
     * Obtiene el estado actual del modo oscuro
     * @returns {boolean} true si está en modo oscuro, false si no
     */
    getDarkMode: function() {
        const darkMode = AgroLocalStorage.get(this.KEYS.DARK_MODE, false);
        console.log('getDarkMode devuelve:', darkMode);
        return darkMode;
    },

    /**
     * Alterna entre modo oscuro y claro
     */
    toggleDarkMode: function() {
        console.log('toggleDarkMode llamado');
        const currentMode = this.getDarkMode();
        console.log('Modo actual:', currentMode);
        this.setDarkMode(!currentMode);
        console.log('Nuevo modo:', !currentMode);
    },

    /**
     * Aplica el modo oscuro según la configuración guardada
     */
    applyDarkMode: function() {
        const isDarkMode = this.getDarkMode();
        console.log('applyDarkMode - isDarkMode:', isDarkMode);
        const htmlElement = document.documentElement;
        
        if (isDarkMode) {
            console.log('Añadiendo clase dark al html');
            htmlElement.classList.add('dark');
        } else {
            console.log('Eliminando clase dark del html');
            htmlElement.classList.remove('dark');
        }
    },

    /**
     * Guarda el último producto visto
     * @param {Object} product - Objeto con información del producto
     */
    setLastViewedProduct: function(product) {
        if (!product || !product.id) return;
        
        // Solo guardamos información básica
        const productInfo = {
            id: product.id,
            name: product.name,
            price: product.price,
            timestamp: new Date().toISOString()
        };
        
        AgroLocalStorage.save(this.KEYS.LAST_VIEWED_PRODUCT, productInfo);
    },

    /**
     * Obtiene el último producto visto
     * @returns {Object|null} Información del último producto visto o null
     */
    getLastViewedProduct: function() {
        return AgroLocalStorage.get(this.KEYS.LAST_VIEWED_PRODUCT, null);
    },

    /**
     * Guarda la última categoría vista
     * @param {Object} category - Objeto con información de la categoría
     */
    setLastViewedCategory: function(category) {
        if (!category || !category.id) return;
        
        const categoryInfo = {
            id: category.id,
            name: category.name,
            timestamp: new Date().toISOString()
        };
        
        AgroLocalStorage.save(this.KEYS.LAST_VIEWED_CATEGORY, categoryInfo);
    },

    /**
     * Obtiene la última categoría vista
     * @returns {Object|null} Información de la última categoría vista o null
     */
    getLastViewedCategory: function() {
        return AgroLocalStorage.get(this.KEYS.LAST_VIEWED_CATEGORY, null);
    },

    /**
     * Establece la preferencia de ítems por página
     * @param {number} count - Número de ítems por página
     */
    setItemsPerPage: function(count) {
        AgroLocalStorage.save(this.KEYS.ITEMS_PER_PAGE, count);
    },

    /**
     * Obtiene la preferencia de ítems por página
     * @returns {number} Número de ítems por página (10 por defecto)
     */
    getItemsPerPage: function() {
        return AgroLocalStorage.get(this.KEYS.ITEMS_PER_PAGE, 10);
    },

    /**
     * Inicializa las preferencias del usuario
     * Debe llamarse cuando la página se carga
     */
    initialize: function() {
        console.log('UserPreferences.initialize() llamado');
        // Aplicar modo oscuro si está configurado
        this.applyDarkMode();
    }
}; 