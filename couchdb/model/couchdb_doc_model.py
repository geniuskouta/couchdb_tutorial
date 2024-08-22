from dataclasses import dataclass

@dataclass
class CouchDBDocModel:
    _id: str
    key: str
    value: dict
    doc: dict

def marshall(entity: dict, document_id: str) -> CouchDBDocModel:
    return CouchDBDocModel(
        _id=document_id,
        key=document_id,
        value: {},
        doc: entity
    )

def unmarshall(model: CouchDBDocModel) -> dict:
    return model.doc
