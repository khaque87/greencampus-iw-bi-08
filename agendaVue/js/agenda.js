// La plantilla se compila con Vue; el HTML público conserva atributos estándar.
new Vue({
            el: '#app',
            template: '#agenda-template',
            data: {
                contactos: [
                    {
                        nombre: 'John Doe',
                        email: 'john.doe@deusto.es',
                        telefono: '555555555'
                    }
                ],
                nuevoContacto: {
                    nombre: '',
                    email: '',
                    telefono: ''
                },
                mensajeError: ''
            },
            mounted: function () {
                try {
                    var guardados = localStorage.getItem('agendaVue_contactos');
                    if (guardados) {
                        var datos = JSON.parse(guardados);
                        if (Array.isArray(datos) && datos.every(function (contacto) {
                            return contacto && typeof contacto.nombre === 'string' &&
                                typeof contacto.email === 'string' && typeof contacto.telefono === 'string';
                        })) {
                            this.contactos = datos;
                        } else {
                            this.mensajeError = 'Los contactos guardados no tienen un formato válido.';
                        }
                    }
                } catch (e) {
                    this.mensajeError = 'No se han podido leer los contactos guardados.';
                }
            },
            methods: {
                guardarEnLocalStorage: function () {
                    try {
                        localStorage.setItem('agendaVue_contactos', JSON.stringify(this.contactos));
                    } catch (e) {
                        this.mensajeError = 'El cambio se ha hecho, pero el navegador no permite guardarlo para la próxima visita.';
                    }
                },
                anadirContacto: function () {
                    if (!this.nuevoContacto.nombre || !this.nuevoContacto.email || !this.nuevoContacto.telefono) {
                        this.mensajeError = 'Por favor, rellena todos los campos.';
                        return;
                    }
                    this.contactos.push({
                        nombre: this.nuevoContacto.nombre,
                        email: this.nuevoContacto.email,
                        telefono: this.nuevoContacto.telefono
                    });
                    this.nuevoContacto.nombre = '';
                    this.nuevoContacto.email = '';
                    this.nuevoContacto.telefono = '';
                    this.mensajeError = '';
                    this.guardarEnLocalStorage();
                },
                borrarContacto: function (index) {
                    this.contactos.splice(index, 1);
                    this.guardarEnLocalStorage();
                }
            }
        });
