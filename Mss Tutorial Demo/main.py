import click
import subprocess

# Dictionary to map shape names to corresponding time intervals in the video
shape_intervals = {
    'sphere': (0, 10),
    'cube': (11, 23),
    'pyramid': (24, 32),
    'cone': (33, 38),
    'cylinder': (39, 43)
}

@click.command()
@click.option('--shape', type=click.Choice(['sphere', 'cube', 'pyramid', 'cone', 'cylinder']), help='Choose a shape to extract from the video')
def extract_shape(shape):
    """Extracts a specific shape from the input video."""
    input_video = "TutorialTest.mp4"
    interval = shape_intervals.get(shape)
    if interval:
        output_video = f"{shape}_extracted.mp4"
        subprocess.run(['ffmpeg', '-i', input_video, '-ss', str(interval[0]), '-to', str(interval[1]), '-c', 'copy', output_video])
        click.echo(f"Extracted {shape} shape from the video.")
        click.echo(f"Showing {shape} shape video...")
        subprocess.run(['ffplay', output_video])
    else:
        click.echo("Shape interval not found.")

if __name__ == '__main__':
    extract_shape()
