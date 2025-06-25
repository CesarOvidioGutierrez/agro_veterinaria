/**
 * Utilidades para manejar localStorage en la aplicación de Agro Veterinaria
 */

const AgroLocalStorage = {
    /**
     * Guarda un valor en localStorage
     * @param {string} key - Clave para almacenar el valor
     * @param {any} value - Valor a almacenar (se convertirá a JSON)
     */
    save: function(key, value) {
        try {
            const serializedValue = JSON.stringify(value);
            localStorage.setItem(key, serializedValue);
            return true;
        } catch (error) {
            console.error('Error al guardar en localStorage:', error);
            return false;
        }
    },

    /**
     * Obtiene un valor desde localStorage
     * @param {string} key - Clave del valor a recuperar
     * @param {any} defaultValue - Valor por defecto si no existe la clave
     * @returns {any} El valor almacenado o el valor por defecto
     */
    get: function(key, defaultValue = null) {
        try {
            const serializedValue = localStorage.getItem(key);
            if (serializedValue === null) {
                return defaultValue;
            }
            return JSON.parse(serializedValue);
        } catch (error) {
            console.error('Error al recuperar de localStorage:', error);
            return defaultValue;
        }
    },

    /**
     * Elimina un valor de localStorage
     * @param {string} key - Clave a eliminar
     */
    remove: function(key) {
        try {
            localStorage.removeItem(key);
            return true;
        } catch (error) {
            console.error('Error al eliminar de localStorage:', error);
            return false;
        }
    },

    /**
     * Limpia todo el localStorage
     */
    clear: function() {
        try {
            localStorage.clear();
            return true;
        } catch (error) {
            console.error('Error al limpiar localStorage:', error);
            return false;
        }
    },

    /**
     * Verifica si existe una clave en localStorage
     * @param {string} key - Clave a verificar
     * @returns {boolean} true si existe, false si no
     */
    exists: function(key) {
        return localStorage.getItem(key) !== null;
    }
}; 