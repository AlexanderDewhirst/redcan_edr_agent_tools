echo "Executing command."

file_name=$1
logger_file_name=$2
initial_data=$3
updated_data=$4

case "$OSTYPE" in
  solaris*)
    echo "SOLARIS"
    ;;
  darwin*)
    echo "OSX"
    python3 ./main.py 
    ;; 
  linux*)
    echo "LINUX"
    ;;
  bsd*)
    echo "BSD"
    ;;
  msys*)
    echo "WINDOWS"
    ;;
  *)
    echo "unknown: $OSTYPE"
    ;;
esac
