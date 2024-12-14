from fastapi import HTTPException, status


def check_file_type_csv(filename: str):
    '''Check file type is .csv'''
    if not filename.endswith('.csv'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='THIS FILE TYPE IS NOT ALLOWED.'
        )
