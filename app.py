import gradio as gr
from seismic_moment_magnitude_calculator import calculate_moment_magnitude

def run_calculation(length_km, width_km, slip_m, shear_mod_gpa):
    try:
        moment_n_m, moment_dyne_cm, magnitude = calculate_moment_magnitude(
            length_km, width_km, slip_m, shear_mod_gpa
        )
        moment_output = f"M0 = {moment_n_m:.2e} N·m ({moment_dyne_cm:.2e} dyne·cm)"
        magnitude_output = f"{magnitude:.2f}"
        return moment_output, magnitude_output
    except Exception as e:
        return f"Error: {str(e)}", "Error"

with gr.Blocks() as demo:
    gr.Markdown("# Seismic Moment Magnitude Calculator")
    gr.Markdown("Calculate earthquake moment magnitude from fault rupture parameters.")
    
    with gr.Column():
        length_input = gr.Number(label="Fault Rupture Length (km)", value=50.0)
        width_input = gr.Number(label="Fault Width (km)", value=20.0)
        slip_input = gr.Number(label="Average Slip (m)", value=1.5)
        shear_mod_input = gr.Number(label="Crustal Shear Modulus (GPa)", value=30.0)
        
        run_button = gr.Button("Run Calculation")
        
        moment_output = gr.Textbox(label="Seismic Moment (M0)")
        magnitude_output = gr.Textbox(label="Moment Magnitude (Mw)")

    run_button.click(
        fn=run_calculation,
        inputs=[length_input, width_input, slip_input, shear_mod_input],
        outputs=[moment_output, magnitude_output]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
