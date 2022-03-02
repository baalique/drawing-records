from app.domain.entities.protocols import HasId


def is_id_equals(entity: HasId, to: int) -> bool:
    return entity.id == to
