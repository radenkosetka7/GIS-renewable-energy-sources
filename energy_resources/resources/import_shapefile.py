from .custom_layer_mapping import CustomLayerMapping


def import_shapefile(filepath, user_req, mapping, model, source_srid,serializer):
    lm = CustomLayerMapping(
        model=model,
        data=filepath,
        mapping=mapping,
        source_srs=source_srid,
        transaction_mode='commit_on_success',
        transform=False,
        last_user=user_req,
        serializer_class=serializer)
    lm.save(verbose=True, strict=True)
