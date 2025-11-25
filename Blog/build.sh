# build.sh - Script que Render ejecutará durante el despliegue

set -o errexit  # ⚠️ Si algún comando falla, que se detenga todo

echo "=== 🚀 INICIANDO CONSTRUCCIÓN ==="

echo "1. 📦 Instalando dependencias..."
pip install -r requirements.txt

echo "2. 📁 Colectando archivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "3. 🗃️ Aplicando migraciones de base de datos..."
python manage.py migrate

# Create a superuser non-interactively if the environment variable is set
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser --no-input
fi

echo "=== ✅ CONSTRUCCIÓN COMPLETADA ==="