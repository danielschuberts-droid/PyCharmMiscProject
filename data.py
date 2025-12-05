"""Data structures for hydrogen plant inputs.

This module defines structured representations for two 100 MW electrolysis
configurations (AEC and PEM) using the provided technical and financial
parameters. The values are preserved as given (percentages, €/units, etc.) so
they can be reused in later calculations.
"""
from dataclasses import asdict, dataclass
from typing import Optional


@dataclass(frozen=True)
class InputData:
    electricity_pct_total_input_mwh: float
    heat_pct_total_input_mwh: Optional[float]
    heat_loss_pct_total_input_mwh: float
    water_for_electrolysis_kg_per_mwh_input: float


@dataclass(frozen=True)
class OutputData:
    hydrogen_output_pct_total_output_mwh: float
    hydrogen_ch2_pct_total_output: float
    hydrogen_for_district_heating_pct_points_of_heat_loss: float
    oxygen_output_pct_total_output_mwh: float
    oxygen_recovered_for_district_heating_pct_points_of_heat_loss: float
    heat_output_pct_total_output_mwh: float
    hydrogen_yield_kg_per_mwh_input_e: float
    oxygen_yield_kg_per_mwh_input_e: float


@dataclass(frozen=True)
class EnergyTechnicalData:
    total_plant_size_mw_input_e: float
    planned_outage_days_per_annum: float
    technical_lifetime_years: float
    input: InputData
    output: OutputData


@dataclass(frozen=True)
class FinancialData:
    specific_investment_eur_per_kw_total_input: float
    specific_investment_eur_per_kg_per_hour_hydrogen_output: float
    o_and_m_pct_of_specific_investment_per_year: float


@dataclass(frozen=True)
class TechnologySpecificData:
    current_density_a_per_cm2: float
    footprint_m2_per_mw_input_e: float
    degradation_rate_pct_per_annum: float
    frequency_of_stack_replacement_years: float


@dataclass(frozen=True)
class PlantConfiguration:
    name: str
    energy_technical: EnergyTechnicalData
    financial: FinancialData
    technology_specific: TechnologySpecificData


# Data instances sourced from the provided table.
AEC_100MW_ENS_2025 = PlantConfiguration(
    name="AEC 100 MW (ENS, 2025)",
    energy_technical=EnergyTechnicalData(
        total_plant_size_mw_input_e=100.0,
        planned_outage_days_per_annum=20.0,
        technical_lifetime_years=20.0,
        input=InputData(
            electricity_pct_total_input_mwh=100.0,
            heat_pct_total_input_mwh=None,
            heat_loss_pct_total_input_mwh=0.0,
            water_for_electrolysis_kg_per_mwh_input=89.15,
        ),
        output=OutputData(
            hydrogen_output_pct_total_output_mwh=58.7,
            hydrogen_ch2_pct_total_output=32.3,
            hydrogen_for_district_heating_pct_points_of_heat_loss=26.4,
            oxygen_output_pct_total_output_mwh=40.9,
            oxygen_recovered_for_district_heating_pct_points_of_heat_loss=0.0,
            heat_output_pct_total_output_mwh=0.4,
            hydrogen_yield_kg_per_mwh_input_e=20.00,
            oxygen_yield_kg_per_mwh_input_e=141.79,
        ),
    ),
    financial=FinancialData(
        specific_investment_eur_per_kw_total_input=1161.3,
        specific_investment_eur_per_kg_per_hour_hydrogen_output=5585.15,
        o_and_m_pct_of_specific_investment_per_year=15.0,
    ),
    technology_specific=TechnologySpecificData(
        current_density_a_per_cm2=0.5,
        footprint_m2_per_mw_input_e=10_000.0,
        degradation_rate_pct_per_annum=0.125,
        frequency_of_stack_replacement_years=10.0,
    ),
)

PEM_100MW_ENS_2025 = PlantConfiguration(
    name="PEM 100 MW (ENS, 2025)",
    energy_technical=EnergyTechnicalData(
        total_plant_size_mw_input_e=100.0,
        planned_outage_days_per_annum=20.0,
        technical_lifetime_years=20.0,
        input=InputData(
            electricity_pct_total_input_mwh=100.0,
            heat_pct_total_input_mwh=None,
            heat_loss_pct_total_input_mwh=0.0,
            water_for_electrolysis_kg_per_mwh_input=91.82,
        ),
        output=OutputData(
            hydrogen_output_pct_total_output_mwh=73.3,
            hydrogen_ch2_pct_total_output=25.0,
            hydrogen_for_district_heating_pct_points_of_heat_loss=30.0,
            oxygen_output_pct_total_output_mwh=25.7,
            oxygen_recovered_for_district_heating_pct_points_of_heat_loss=0.0,
            heat_output_pct_total_output_mwh=1.0,
            hydrogen_yield_kg_per_mwh_input_e=20.95,
            oxygen_yield_kg_per_mwh_input_e=148.53,
        ),
    ),
    financial=FinancialData(
        specific_investment_eur_per_kw_total_input=1368.2,
        specific_investment_eur_per_kg_per_hour_hydrogen_output=6876.8,
        o_and_m_pct_of_specific_investment_per_year=15.0,
    ),
    technology_specific=TechnologySpecificData(
        current_density_a_per_cm2=2.0,
        footprint_m2_per_mw_input_e=7_000.0,
        degradation_rate_pct_per_annum=0.125,
        frequency_of_stack_replacement_years=6.0,
    ),
)

PLANT_CONFIGURATIONS = [AEC_100MW_ENS_2025, PEM_100MW_ENS_2025]


def as_dict_list():
    """Return plant configurations as a list of dictionaries."""
    return [asdict(config) for config in PLANT_CONFIGURATIONS]
