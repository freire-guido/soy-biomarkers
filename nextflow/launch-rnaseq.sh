nextflow run nf-core/rnaseq \
	-profile docker,awsbatch \
	-work-dir s3://genomic-nextflow/rnaseq/work \
	--awsqueue genomic-nextflow-queue \
	--awsregion us-east-1 \
	--input s3://genomic-nextflow/fetchngs/output/samplesheet/samplesheet.csv \
	--outdir s3://genomic-nextflow/rnaseq/output/ \
	--genome Gm01