class InvalidShapeFileError(Exception):

    def __init__(self, *args):
        default_message = 'Shapefile is not valid'
        if not args:
            args = (default_message,)
        super(InvalidShapeFileError, self).__init__(*args)
