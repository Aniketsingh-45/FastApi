# Pydantic Examples

This directory contains various examples demonstrating the usage and capabilities of the [Pydantic](https://docs.pydantic.dev/) library for data validation and settings management in Python. 

These scripts serve as a learning resource and reference for different Pydantic features, from basic type checking to complex custom validations.

## Contents

- **`_pydantic_why.py`**: A basic script explaining the necessity of Pydantic for robust data validation compared to manual type checking.
- **`pydantic_model.py`**: Demonstrates simple type validation by defining a basic `Patient` model inheriting from `BaseModel`.
- **`pydantic_main.py`**: Shows advanced data validation using `Field` and `Annotated` for adding constraints (e.g., `max_length`, `gt`, `lt`) and metadata to model fields.
- **`_field_validator.py`**: Illustrates how to apply custom validation logic to specific fields using the `@field_validator` decorator (e.g., validating email domains or value ranges).
- **`_model_validator.py`**: Demonstrates the use of the `@model_validator` decorator to apply validation rules that depend on multiple fields within the model (e.g., conditional validation based on age).
- **`_computed_field.py`**: Shows how to use the `@computed_field` decorator to create properties that are dynamically calculated based on other fields (e.g., calculating BMI from height and weight).
- **`nested_model.py`**: Provides an example of composing models by nesting them within each other (e.g., an `Address` model inside a `Patient` model).
- **`serialization.py`**: Covers model serialization, demonstrating how to convert Pydantic models back into dictionaries (`model_dump()`) or JSON strings (`model_dump_json()`).

## Running the Examples

You can run any of the scripts directly using Python. For example:

```bash
python pydantic_main.py
```
