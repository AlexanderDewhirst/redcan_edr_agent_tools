function push_content_to_file() {
    content=$1
    location=$2
    echo $content >> $location
}

function replace_content_in_file() {
    content_to_replace=$1
    replace_with_content=$2
    location=$3
    sed -e "s/$content_to_replace/$replace_content_with/g" $location
}

function delete_file() {
    location=$1
    rm $location
}


## from another bash script
# source ./file_utils.sh

# push_content_to_file $initial_data $file_name
# cat $file_name
# push_content_to_file "Logger: Pushing $initial_data to $file_name" $logger_file_name

# push_content_to_file $updated_data $file_name
# cat $file_name
# push_content_to_file "Logger: Replacing $initial_data to $updated_data in $file_name" $logger_file_name

# delete_file $file_name
# push_content_to_file "Logger: Deleting $file_name" $logger_file_name
